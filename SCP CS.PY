import dearpygui.dearpygui as dpg
import os
import json
import time

CONFIG_DIR = os.path.join(os.path.expanduser("~"), "Documents", "inerium")
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

def save_config(filename):
    """Сохранить конфигурацию в файл."""
    config = {
        "aim_enable": dpg.get_value("aim_enable"),
        "weapon_selection": dpg.get_value("weapon_selection"),
        "aim_type": dpg.get_value("aim_type"),
        "draw_fov": dpg.get_value("draw_fov"),
        "fov_scale": dpg.get_value("fov_scale"),
        "auto_loot": dpg.get_value("auto_loot"),
        "item_selection": dpg.get_value("item_selection"),
        "fly": dpg.get_value("fly"),
        "fly_speed": dpg.get_value("fly_speed"),
        "speedhax": dpg.get_value("speedhax"),
        "godmode": dpg.get_value("godmode"),
        "noclip": dpg.get_value("noclip"),
        "noclip_speed": dpg.get_value("noclip_speed"),
        "bunnyhop": dpg.get_value("bunnyhop"),
        "jump": dpg.get_value("jump"),
        "friendlyfire": dpg.get_value("friendlyfire"),
        "fire_rate": dpg.get_value("fire_rate"),
        "rcs_control_x": dpg.get_value("rcs_control_x"),
        "rcs_control_y": dpg.get_value("rcs_control_y"),
        "rcs_control_z": dpg.get_value("rcs_control_z"),
        "bypass": dpg.get_value("bypass"),
        "vanilla_plug": dpg.get_value("vanilla_plug")
    }
    try:
        with open(os.path.join(CONFIG_DIR, filename), 'w') as file:
            json.dump(config, file, indent=4)
        print(f"Config saved: {filename}")
        update_config_list()  # Обновляем список конфигураций после сохранения
    except Exception as e:
        print(f"Error saving config: {e}")

def load_config(filename):
    """Загрузить конфигурацию из файла."""
    try:
        with open(os.path.join(CONFIG_DIR, filename), 'r') as file:
            config = json.load(file)
            for key, value in config.items():
                if dpg.does_item_exist(key):
                    dpg.set_value(key, value)
        print(f"Loaded config data: {filename}")
    except FileNotFoundError:
        print("Config file not found")
    except Exception as e:
        print(f"Error loading config: {e}")

def list_configs():
    """Получить список конфигурационных файлов."""
    return [f for f in os.listdir(CONFIG_DIR) if f.endswith(".json")]

def update_config_list():
    """Обновить список конфигураций в интерфейсе."""
    # Сначала удаляем старые элементы
    dpg.configure_item("config_list", items=list_configs())

def delete_config(filename):
    """Удалить конфигурацию из файла."""
    try:
        os.remove(os.path.join(CONFIG_DIR, filename))
        update_config_list()  # Обновляем список конфигураций после удаления
        print(f"Deleted config: {filename}")
    except Exception as e:
        print(f"Error deleting config: {e}")

def setup_gui():
    dpg.create_context()
    dpg.create_viewport(title='Game Cheat Menu', width=800, height=600, resizable=False)
    dpg.setup_dearpygui()

    # Add key handler for toggling viewport visibility
    with dpg.handler_registry():
        dpg.add_key_down_handler(key=dpg.mvKey_Insert, callback=lambda s, a: toggle_viewport())

    # Create main window with tabs
    with dpg.window(label="INERIUM | SCP Classfied Site", width=800, height=600, tag="main_window"):
        with dpg.tab_bar():
            # Aim tab
            with dpg.tab(label="Aim"):
                dpg.add_checkbox(label="Aim Enable", tag="aim_enable")
                dpg.add_combo(label="Weapon", items=["Pistol", "Rifles", "SMGs"], tag="weapon_selection")
                dpg.add_combo(label="Aim Type", items=["Silent", "Auto", "pSilent"], tag="aim_type")
                dpg.add_checkbox(label="Draw FOV", tag="draw_fov")
                dpg.add_slider_float(label="FOV Scale", default_value=1.0, min_value=0.1, max_value=10.0, tag="fov_scale")

            # Player tab
            with dpg.tab(label="Player"):
                dpg.add_checkbox(label="Auto Loot", tag="auto_loot")
                dpg.add_combo(label="Item Selection", items=["Card 1", "Card 2", "Card 4", "Card 5", "Card 6", "Weapon"], tag="item_selection")
                dpg.add_checkbox(label="Fly", tag="fly")
                dpg.add_slider_float(label="Fly Speed", default_value=1.0, min_value=0.1, max_value=10.0, tag="fly_speed")
                dpg.add_checkbox(label="Speedhax", tag="speedhax")
                dpg.add_checkbox(label="Godmode (BUG)", tag="godmode")
                dpg.add_checkbox(label="Noclip", tag="noclip")
                dpg.add_slider_float(label="Noclip Speed", default_value=1.0, min_value=0.1, max_value=10.0, tag="noclip_speed")
                dpg.add_checkbox(label="Bunnyhop", tag="bunnyhop")
                dpg.add_checkbox(label="Jump", tag="jump")
                dpg.add_checkbox(label="FriendlyFire", tag="friendlyfire")
                dpg.add_slider_float(label="FireRate", default_value=1.0, min_value=0.1, max_value=10.0, tag="fire_rate")
                dpg.add_slider_float(label="RCS Control X", default_value=1.0, min_value=0.1, max_value=10.0, tag="rcs_control_x")
                dpg.add_slider_float(label="RCS Control Y", default_value=1.0, min_value=0.1, max_value=10.0, tag="rcs_control_y")
                dpg.add_slider_float(label="RCS Control Z", default_value=1.0, min_value=0.1, max_value=10.0, tag="rcs_control_z")

            # Antiban tab
            with dpg.tab(label="Antiban"):
                dpg.add_checkbox(label="Bypass", tag="bypass")
                dpg.add_checkbox(label="Vanilla Plug", tag="vanilla_plug")

            # Config tab
            with dpg.tab(label="Config"):
                dpg.add_input_text(label="Config Name", tag="config_name", default_value="config.json")
                dpg.add_button(label="Save Config", callback=lambda: save_config(dpg.get_value("config_name")))
                dpg.add_button(label="Load Config", callback=lambda: load_config(dpg.get_value("config_name")))
                dpg.add_button(label="Refresh List", callback=update_config_list)
                dpg.add_listbox(label="Config List", items=list_configs(), tag="config_list")
                dpg.add_button(label="Delete Config", callback=lambda: delete_config(dpg.get_value("config_list")))

    dpg.show_viewport()

    # Main loop
    try:
        while True:
            dpg.render_dearpygui_frame()
            time.sleep(0.05)
    except KeyboardInterrupt:
        dpg.destroy_context()

def toggle_viewport():
    """Toggle the visibility of the viewport."""
    viewport = dpg.get_viewport()
    if viewport['visible']:
        dpg.hide_viewport()
    else:
        dpg.show_viewport()

if __name__ == "__main__":
    setup_gui()

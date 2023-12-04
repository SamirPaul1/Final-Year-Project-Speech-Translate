import os

# Paths
dir_project: str = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__))))
dir_user: str = os.path.abspath(os.path.join(dir_project, "_user"))
dir_theme: str = os.path.abspath(os.path.join(dir_project, "theme"))
dir_temp: str = os.path.abspath(os.path.join(dir_project, "temp"))
dir_debug: str = os.path.abspath(os.path.join(dir_project, "debug"))
dir_log: str = os.path.abspath(os.path.join(dir_project, "log"))
dir_assets: str = os.path.abspath(os.path.join(dir_project, "assets"))
dir_export: str = os.path.abspath(os.path.join(dir_project, "export"))
dir_refinement: str = os.path.abspath(os.path.join(dir_export, "@refined"))
dir_translate: str = os.path.abspath(os.path.join(dir_export, "@translated"))
dir_alignment: str = os.path.abspath(os.path.join(dir_export, "@aligned"))
p_app_icon: str = os.path.abspath(os.path.join(dir_assets, "icon.ico"))
p_splash_image: str = os.path.abspath(os.path.join(dir_assets, "splash.png"))
p_parameters_text: str = os.path.abspath(os.path.join(dir_assets, "parameter.txt"))
p_base_filter: str = os.path.abspath(os.path.join(dir_assets, "base_hallucination_filter.json"))
p_ffmpeg_ps_script: str = os.path.abspath(os.path.join(dir_project, "..", "install_ffmpeg.ps1"))
p_filter_rec: str = os.path.abspath(os.path.join(dir_user, "hallucination_filter_record.json"))
p_filter_file_import: str = os.path.abspath(os.path.join(dir_user, "hallucination_filter_file_import.json"))

# verify app_icon exist or not
if not os.path.exists(p_app_icon):
    app_icon_missing = True
else:
    app_icon_missing = False

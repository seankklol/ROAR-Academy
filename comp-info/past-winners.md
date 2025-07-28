Directory structure:
└── derekchen1-roarcompetition/
    ├── README.md
    ├── competition_code/
    │   ├── collectBaseWaypoints.py
    │   ├── competition_runner.py
    │   ├── debugCompetitionRunner.py
    │   ├── debugDataReader.py
    │   ├── drawWaypoints.py
    │   ├── infrastructure.py
    │   ├── infrastructure_debug.py
    │   ├── LateralController.py
    │   ├── SpeedData.py
    │   ├── submission.py
    │   ├── ThrottleController.py
    │   ├── waypoint_collect.py
    │   ├── waypointRemover.py
    │   ├── waypointSplicer.py
    │   ├── configs/
    │   │   └── LatPIDConfig.json
    │   ├── debugData/
    │   │   └── debugData.json
    │   └── waypoints/
    │       ├── Monza Original Waypoints.npz
    │       ├── waypointsPrimary.npz
    │       └── archive/
    │           ├── oldWaypointsPrimary.npz
    │           ├── oldWaypointsPrimary2.npz
    │           ├── oldWaypointsPrimary3.npz
    │           └── oldWaypointsPrimary4.npz
    └── experimental_competition_code/
        ├── collectBaseWaypoints.py
        ├── competition_runner.py
        ├── debugCompetitionRunner.py
        ├── debugDataReader.py
        ├── drawWaypoints.py
        ├── findCorners.py
        ├── infrastructure.py
        ├── infrastructure_debug.py
        ├── LateralController.py
        ├── SpeedData.py
        ├── submission.py
        ├── ThrottleController.py
        ├── waypoint_collect.py
        ├── waypointRemover.py
        ├── waypointSplicer.py
        ├── configs/
        │   └── LatPIDConfig.json
        ├── debugData/
        │   └── debugData.json
        ├── global_racetrajectory_optimization-master/
        │   ├── Readme.md
        │   ├── LICENSE
        │   ├── main_gen_frictionmap.py
        │   ├── main_globaltraj.py
        │   ├── requirements.txt
        │   ├── frictionmap/
        │   │   ├── __init__.py
        │   │   └── src/
        │   │       ├── __init__.py
        │   │       ├── plot_frictionmap_data.py
        │   │       ├── plot_frictionmap_grid.py
        │   │       └── reftrack_functions.py
        │   ├── helper_funcs_glob/
        │   │   ├── __init__.py
        │   │   └── src/
        │   │       ├── __init__.py
        │   │       ├── calc_min_bound_dists.py
        │   │       ├── check_traj.py
        │   │       ├── export_traj_ltpl.py
        │   │       ├── export_traj_race.py
        │   │       ├── import_track.py
        │   │       ├── interp_track.py
        │   │       ├── prep_track.py
        │   │       └── result_plots.py
        │   ├── inputs/
        │   │   ├── frictionmaps/
        │   │   │   ├── berlin_2018_tpadata.json
        │   │   │   ├── berlin_2018_tpamap.csv
        │   │   │   ├── berlin_2018_varmue08-12_tpadata.json
        │   │   │   ├── berlin_2018_varmue09-11_tpadata.json
        │   │   │   ├── handling_track_tpadata.json
        │   │   │   ├── handling_track_tpamap.csv
        │   │   │   ├── modena2019_tpadata.json
        │   │   │   ├── modena2019_tpamap.csv
        │   │   │   ├── rounded_rectangle_tpadata.json
        │   │   │   └── rounded_rectangle_tpamap.csv
        │   │   ├── tracks/
        │   │   │   ├── berlin_2018.csv
        │   │   │   ├── handling_track.csv
        │   │   │   ├── modena_2019.csv
        │   │   │   └── rounded_rectangle.csv
        │   │   └── veh_dyn_info/
        │   │       ├── ax_max_machines.csv
        │   │       └── ggv.csv
        │   ├── opt_mintime_traj/
        │   │   ├── Readme.md
        │   │   ├── __init__.py
        │   │   ├── powertrain_src/
        │   │   │   ├── Readme.md
        │   │   │   ├── __init__.py
        │   │   │   ├── component_losses.PNG
        │   │   │   ├── component_temperatures.PNG
        │   │   │   └── src/
        │   │   │       ├── __init__.py
        │   │   │       ├── Battery.py
        │   │   │       ├── EMachine.py
        │   │   │       ├── Inverter.py
        │   │   │       └── Radiators.py
        │   │   └── src/
        │   │       ├── __init__.py
        │   │       ├── approx_friction_map.py
        │   │       ├── export_mintime_solution.py
        │   │       ├── extract_friction_coeffs.py
        │   │       ├── friction_map_interface.py
        │   │       ├── friction_map_plot.py
        │   │       ├── opt_mintime.py
        │   │       └── result_plots_mintime.py
        │   ├── params/
        │   │   └── racecar.ini
        │   └── trajectory_planning_helpers-master/
        │       ├── README.md
        │       ├── LICENSE
        │       ├── requirements.txt
        │       ├── setup.py
        │       ├── example_files/
        │       │   ├── ax_max_machines.csv
        │       │   ├── berlin_2018.csv
        │       │   └── ggv.csv
        │       └── trajectory_planning_helpers/
        │           ├── __init__.py
        │           ├── angle3pt.py
        │           ├── calc_ax_profile.py
        │           ├── calc_head_curv_an.py
        │           ├── calc_head_curv_num.py
        │           ├── calc_normal_vectors.py
        │           ├── calc_normal_vectors_ahead.py
        │           ├── calc_spline_lengths.py
        │           ├── calc_splines.py
        │           ├── calc_t_profile.py
        │           ├── calc_tangent_vectors.py
        │           ├── calc_vel_profile.py
        │           ├── calc_vel_profile_brake.py
        │           ├── check_normals_crossing.py
        │           ├── conv_filt.py
        │           ├── create_raceline.py
        │           ├── get_rel_path_part.py
        │           ├── import_veh_dyn_info.py
        │           ├── import_veh_dyn_info_2.py
        │           ├── interp_splines.py
        │           ├── interp_track.py
        │           ├── interp_track_widths.py
        │           ├── iqp_handler.py
        │           ├── nonreg_sampling.py
        │           ├── normalize_psi.py
        │           ├── opt_min_curv.py
        │           ├── opt_shortest_path.py
        │           ├── path_matching_global.py
        │           ├── path_matching_local.py
        │           ├── progressbar.py
        │           ├── side_of_line.py
        │           └── spline_approximation.py
        └── waypoints/
            ├── monzaOriginalWaypoints.npz
            ├── waypointsPrimary.npz
            └── archive/
                ├── oldWaypointsPrimary.npz
                ├── oldWaypointsPrimary2.npz
                ├── oldWaypointsPrimary3.npz
                └── oldWaypointsPrimary4.npz

ThesisCodeDataset/
├── dataprocess/
│   ├── kinematic_kinatic/
│   └── pythoncode/
├── SCONE_scenario/
│   ├── data/
│   │   ├── init_files/
│   │   │   ├── OtherInitialGuess/
│   │   │   └── 0314KS0000060.par
│   │   ├── HfdConfigPlanarMotorCollisionV2.zml
│   │   ├── InitialState.zml
│   │   ├── P1242_C101.sto
│   │   ├── RF1_H1120_STW_2023_kl_kf_kv_vest_deleteM.scone
│   │   ├── RF2_H1120_STW_2023_kl_kf_kv_vest_deleteM.scone
│   │   ├── RF3_H1120_STW_2023_kl_kf_kv_vest_deleteM.scone
│   │   └── semifinalHFDKS0.hfd
│   ├── otherScenario/
│   └── Final_00_threshold.scone
└── readme.txt


1. dataprocess/:
		This directory contains scripts and data files related to data processing.

	kinematic_kinatic/:
		Contains files related to kinematic and kinetic data (simulation results) processing.

	pythoncode/:
		Contains Python scripts used for various data processing and plotting tasks.

2. SCONE_scenario/:
		This directory holds scenarios for the SCONE framework.

	Final_00_threshold.scone:
		A specific SCONE scenario configuration file. This example file should be able used directly for simulation and optimization.


	data/:
		Contains model, initialization files necessary for running SCONE scenarios.

	init_files/:
		Contains initialization files required for scenarios.

	OtherInitialGuess/:
		Subdirectory for other initial guess parameter files.

	0314KS0000060.par:
		A specific parameter file for initial guess.

	HfdConfigPlanarMotorCollisionV2.zml:
		Configuration file for planar motor collision.

	InitialState.zml:
		Initial state (posture) configuration file.

	P1242_C101.sto:
		Kinematic and kinetic data for validation.

	RF1_H1120_STW_2023_kl_kf_kv_vest_deleteM.scone:
		SCONE reflex controller file.

	RF2_H1120_STW_2023_kl_kf_kv_vest_deleteM.scone:
		SCONE reflex controller file.

	RF3_H1120_STW_2023_kl_kf_kv_vest_deleteM.scone:
		SCONE reflex controller file.

	semifinalHFDKS0.hfd:
		Hyfydy model file (prosthetic model).

	otherScenario/:
		Contains additional scenarios for the SCONE framework.


Notes:

Make sure to update paths and parameters in the SCONE.scenario files or python.

**Hyfydy license required**

SCONE: https://scone.software/doku.php?id=start
Hyfydy: https://hyfydy.com/
# kpi-validation
Scripts and Github Actions workflows to validate part of the KPIs set for OASEES.

For an extended report and detailed explanation on the tests carried out for the KPIs, refer to [OASEES_KPIs_report.pdf](https://github.com/oasees/kpi-validation/blob/main/evidence/OASEES_KPIs_report.pdf) 

This repo currently covers the following KPIs:

| **KPIs**  | **Source**  | **Workflow File** | **Evidence / Workflow Output** |
|---|---|---|---|
| < 2 sec Service deployment time  | [deployment_time](https://github.com/oasees/kpi-validation/tree/main/deployment_time)  | [link](https://github.com/oasees/kpi-validation/blob/main/.github/workflows/deployment_time.yml)  | [link](https://github.com/oasees/kpi-validation/tree/main/evidence/Deployment_time/run-20231095718) |
| \>= 3 distributed components <br> of the same service  | [distributed_service](https://github.com/oasees/kpi-validation/tree/main/distributed_service/manifests)  | [link](https://github.com/oasees/kpi-validation/blob/main/.github/workflows/distributed_service.yml)  | [link](https://github.com/oasees/kpi-validation/tree/main/evidence/Distributed_service/run-20173415013) |
| \>= 50 concurrent services running  | [concurrent_nodes_services/deployments](https://github.com/oasees/kpi-validation/tree/main/concurrent_nodes_services/deployments) | [link](https://github.com/oasees/kpi-validation/blob/main/.github/workflows/concurrent_node_services.yml) | [link](https://github.com/oasees/kpi-validation/tree/main/evidence/Concurrent_nodes_and_services/run-20173371746) |
| \>= 50 edge nodes managed <br> by the same OASEES instance  | [concurrent_nodes_services/nodes](https://github.com/oasees/kpi-validation/tree/main/concurrent_nodes_services/nodes)  | [link](https://github.com/oasees/kpi-validation/blob/main/.github/workflows/concurrent_node_services.yml)  | [link](https://github.com/oasees/kpi-validation/tree/main/evidence/Concurrent_nodes_and_services/run-20173371746) |
| Demonstration of multi-domain edge services <br> with >= 3 OASEES instances  | - | - | [link](https://github.com/oasees/kpi-validation/blob/main/evidence/OASEES_KPIs_report.pdf) |
| Marketplace PoC with >= 50 OASEES deployments <br> and capabilities adverstised  | [marketplace_poc](https://github.com/oasees/kpi-validation/tree/main/marketplace_poc)  | [link](https://github.com/oasees/kpi-validation/blob/main/.github/workflows/marketplace_poc.yml) | [link](https://github.com/oasees/kpi-validation/tree/main/evidence/Marketplace_PoC/run-20234334884) |

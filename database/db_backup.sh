#!/bin/bash

here=$(cd $(dirname $0); pwd -P)
pg_dump -h localhost -p 5432 -U wangnan -w -d devops -t git_repo -t publishment -t publishment_staticfile -t publishment_fe_vue -t alembic_version --insert -f "${here}/backup_"$(date '+%Y-%m-%d_%H:%M:%S')".sql"

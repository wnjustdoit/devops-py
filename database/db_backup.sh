#!/bin/bash

pg_dump -h localhost -p 5432 -U wangnan -w -d devops -t git_repo -t publishment -t alembic_version --insert -f "$(pwd)"/backup_"$(date '+%Y-%m-%d_%H:%M:%S')".sql
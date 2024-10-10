# CLI-client

## CLI Commands
To run the client, use the command:
```bash
python3 evgroup_38 scope --params
```

The following command displays all available scopes: 
```bash
python3 evgroup_38 --help
```
to see detailed information about the parameters of a specific `<scope>`, use the command:
```bash
python3 evgroup_38 <scope> --help
```


The available commands are:

    python3 evgroup_38 healthcheck
    python3 evgroup_38 resetsessions
    python3 evgroup_38 login
    python3 evgroup_38 logout
    python3 evgroup_38 SessionsPerPoint --point --datefrom --dateto --format <json/csv>
    python3 evgroup_38 SessionsPerStation --station --datefrom --dateto --format <json/csv>
    python3 evgroup_38 SessionsPerEV --ev --datefrom --dateto --format <json/csv>
    python3 evgroup_38 SessionsPerProvider --provider --datefrom --dateto --format <json/csv>
    python3 evgroup_38 Admin --usermod --create --username --passw
    python3 evgroup_38 Admin --usermod --update --username --passw
    python3 evgroup_38 Admin --users
    python3 evgroup_38 Admin --sessionsupd --source <csv_file_name>
    python3 evgroup_38 Admin --healthcheck
    python3 evgroup_38 Admin --resetsessions

**Note**: For the command `python3 evgroup_38 Admin --sessionsupd --source <csv_file_name>`, the CSV file must be located within the directory the CLI is running.

## Unit Testing
For Unit Testing, run the following command within the `CLI_unit_tests` directory:
```bash
python3 -m unittest -v test_unit_cli
```
## Functional Testing
For Functional Testing, run the following command within the `CLI_functional_tests` directory:
```bash
py.test -v test_functional_cli.py
```

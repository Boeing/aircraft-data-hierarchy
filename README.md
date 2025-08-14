# Aircraft Data Hierarchy

[![Python package](https://github.com/Boeing/aircraft-data-hierarchy/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/Boeing/aircraft-data-hierarchy/actions/workflows/python-package.yml)
[![Test Package](https://github.com/Boeing/aircraft-data-hierarchy/actions/workflows/test-package.yml/badge.svg?branch=main)](https://github.com/Boeing/aircraft-data-hierarchy/actions/workflows/test-package.yml)
[![Build and Deploy Documentation](https://github.com/Boeing/aircraft-data-hierarchy/actions/workflows/sphinx-docs.yml/badge.svg?branch=main)](https://github.com/Boeing/aircraft-data-hierarchy/actions/workflows/sphinx-docs.yml)

The Aircraft Data Hierarchy (ADH) is a modern data definition standard for the aerospace vehicle design studies. The ADH enables engineers to exchange information (i.e. geometry, disciplinary tool inputs/outputs, requirements, etc.) between tools using a common data structure and a schema that can be validated. This structured system allows not only more efficient data transfer within an integrated workflow, but also improved collaboration between entities that utilize the ADH standard. The ADH is specifically architected to align the high-level needs of systems analysis (i.e., MDAO) and systems engineering (i.e., MBSE) including having a recursive structure. It includes modern programming features such as schema definition and validation using pydantic and support for JSON, YAML, and XML persistence files. Utility methods are being developed that will make the reading, writing, and manipulation of the ADH in python simple and straightforward.

To use the ADH you need to use Python 3.8 or higher and Pydantic v2.

The foundational structure of the ADH is provided by Pydantic v2 classes, ensuring a single source of data that is self-validating to manage the quality of the data. This approach makes the complexity of Aircraft Design in a Model-Based Systems Engineering (MBSE) environment more transparent and intuitive.

## Documentation

The documentation and examples for this project are hosted on Github Pages: [Aircraft Data Hierarchy Documentation](https://boeing.github.io/aircraft-data-hierarchy/)

## Contributing

To contribute to the development of the Aircraft Data Hierarchy package begin by forking the repository, then commit and push your changes, and open a pull request. To help us keep track of your contributions please use GitHub issues for new features and bugs. If you need help getting started as a developer review the [contributing](CONTRIBUTING.md) instructions.

## License

Copyright 2025 The Boeing Company.

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

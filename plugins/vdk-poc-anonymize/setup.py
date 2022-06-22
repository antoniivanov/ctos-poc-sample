import pathlib
import setuptools

setuptools.setup(
    name="vdk-poc-anonymize",
    version="1.0",
    description="POC Anonymization plugin",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    install_requires=["vdk-core"],
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    entry_points={
        "vdk.plugin.run": [
            "vdk-poc-anonymize-plugin = vdk.ctos.anonymization_plugin",
        ]
    }
)
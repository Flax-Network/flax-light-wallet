from setuptools import setup

dependencies = [
    "blspy==1.0.6",  # Signature library
    "chiavdf==1.0.3",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.4",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.14",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the flaxlight processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    # Query DNS seeds (unreleased commit)
    "dnspythonchia==2.2.0",
    "packaging==21.0",
    "watchdog==2.1.6",  # Filesystem event watching - watches keyring.yaml
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "types-setuptools",
]

kwargs = dict(
    name="flaxlight-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@flaxnetwork.org",
    description="Flax blockchain full node, farmer, timelord, and wallet.",
    url="https://flaxnetwork.org/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="flaxlight blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "flaxlight",
        "flaxlight.cmds",
        "flaxlight.clvm",
        "flaxlight.consensus",
        "flaxlight.daemon",
        "flaxlight.full_node",
        "flaxlight.timelord",
        "flaxlight.farmer",
        "flaxlight.harvester",
        "flaxlight.introducer",
        "flaxlight.plotting",
        "flaxlight.pools",
        "flaxlight.protocols",
        "flaxlight.rpc",
        "flaxlight.server",
        "flaxlight.simulator",
        "flaxlight.types.blockchain_format",
        "flaxlight.types",
        "flaxlight.util",
        "flaxlight.wallet",
        "flaxlight.wallet.puzzles",
        "flaxlight.wallet.rl_wallet",
        "flaxlight.wallet.cc_wallet",
        "flaxlight.wallet.did_wallet",
        "flaxlight.wallet.settings",
        "flaxlight.wallet.trading",
        "flaxlight.wallet.util",
        "flaxlight.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "flaxlight = flaxlight.cmds.flaxlight:main",
            "flaxlight_wallet = flaxlight.server.start_wallet:main",
            "flaxlight_full_node = flaxlight.server.start_full_node:main",
            "flaxlight_harvester = flaxlight.server.start_harvester:main",
            "flaxlight_farmer = flaxlight.server.start_farmer:main",
            "flaxlight_introducer = flaxlight.server.start_introducer:main",
            "flaxlight_timelord = flaxlight.server.start_timelord:main",
            "flaxlight_timelord_launcher = flaxlight.timelord.timelord_launcher:main",
            "flaxlight_full_node_simulator = flaxlight.simulator.start_simulator:main",
        ]
    },
    package_data={
        "flaxlight": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "flaxlight.util": ["initial-*.yaml", "english.txt"],
        "flaxlight.ssl": ["flaxlight_ca.crt", "flaxlight_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)


from conan.packager import ConanMultiPackager

def main():
    """
    Main function.
    """

    builder = ConanMultiPackager(username="piroxiljin", channel="testing")
    builder.add_common_builds()
    filtered_builds = []
    for settings, options, env_vars, build_requires in builder.builds:
        if settings["compiler"] == "Visual Studio":
            if settings["compiler.runtime"] == "MT" or settings["compiler.runtime"] == "MTd":
                # Ignore MT runtime
                continue
        if settings["arch"] != "x86_64":
            continue

        filtered_builds.append([settings, options, env_vars, build_requires])

    builder.builds = filtered_builds
    builder.run()

if __name__ == "__main__":
    main()

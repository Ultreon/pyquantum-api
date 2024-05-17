package dev.ultreon.pyquantum.wrap;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public abstract class Wrapper {

    public static void buildPath() throws IOException {
        new ClasspathWrapper().build(Paths.get("src/main/python"));
    }

    public abstract void build(Path output) throws IOException;
}
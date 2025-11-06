# Chronologue Android

Android app for the Chronologue time tracking application.

## Setup

1. Open the project in Android Studio by selecting the `android` folder

2. Or build from command line:
   ```bash
   ./gradlew build
   ```

## Running

### Debug Build
```bash
./gradlew assembleDebug
```

### Release Build
```bash
./gradlew assembleRelease
```

### Run on Device/Emulator
```bash
./gradlew installDebug
```

## Testing

### Unit Tests
```bash
./gradlew test
```

### Instrumentation Tests
```bash
./gradlew connectedAndroidTest
```

## Project Structure

- `app/src/main/java/` - Main application code
- `app/src/main/res/` - Resources (layouts, strings, etc.)
- `app/src/test/` - Unit tests
- `app/src/androidTest/` - Instrumentation tests
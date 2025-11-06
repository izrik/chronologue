# AGENTS.md - Chronologue Time Tracker

## Build/Lint/Test Commands

### Backend (FastAPI)
#### Build
- `python -m build` - Build distribution packages
- `python setup.py build` - Alternative build command

#### Test
- `pytest` - Run all tests
- `pytest tests/test_file.py::TestClass::test_method` - Run single test
- `python -m unittest discover` - Alternative test runner

#### Lint & Format
- `flake8 .` - Lint code with flake8

### Web Frontend (React)
#### Build
- `npm run build` - Build production bundle
- `npm run dev` - Start development server

#### Test
- `npm test` - Run all tests
- `npm test -- --testNamePattern="test name"` - Run single test

#### Lint & Format
- `npm run lint` - Lint code
- `npm run format` - Format code

### Android App (vanilla Android SDK)
#### Build
- `./gradlew build` - Build the app
- `./gradlew assembleDebug` - Build debug APK
- `./gradlew assembleRelease` - Build release APK

#### Test
- `./gradlew test` - Run unit tests
- `./gradlew connectedAndroidTest` - Run instrumented tests on device

#### Lint & Format
- `./gradlew lint` - Run Android lint

## Code Style Guidelines

### Backend (FastAPI)
#### Imports
- Use absolute imports over relative imports
- Group imports: standard library, third-party, local
- Sort imports alphabetically within groups

#### Formatting
- Use 4 spaces for indentation
- Line length: 80 characters
- Use single or double quotes for strings

#### Types
- Use type hints for function parameters and return values
- Use `typing` module for complex types

#### Naming Conventions
- Functions/variables: snake_case
- Classes: PascalCase
- Constants: UPPER_SNAKE_CASE
- Private members: leading underscore

#### Error Handling
- Use specific exception types
- Provide meaningful error messages
- Use context managers for resource management

### Web Frontend (React)
#### Imports
- Use ES6 imports/exports
- Group imports: React, third-party libraries, local modules
- Sort imports alphabetically within groups

#### Formatting
- Use 2 spaces for indentation
- Line length: 80 characters
- Use single quotes for strings
- Use semicolons

#### Types
- Use TypeScript for type safety
- Define interfaces for complex objects
- Use union types and generics appropriately

#### Naming Conventions
- Functions/variables: camelCase
- Classes/Components: PascalCase
- Constants: UPPER_SNAKE_CASE
- Private members: leading underscore

#### Error Handling
- Use try/catch blocks for async operations
- Provide user-friendly error messages
- Use error boundaries for React components

### Android App (vanilla Android SDK)
#### Imports
- Use Java import statements
- Group imports: Android framework, third-party libraries, local packages
- Sort imports alphabetically

#### Formatting
- Use 4 spaces for indentation
- Line length: 100 characters (Android standard)
- Follow Android code style guidelines

#### Types
- Use appropriate Java types
- Define data classes/interfaces for complex objects
- Use generics appropriately

#### Naming Conventions
- Classes: PascalCase
- Methods/variables: camelCase
- Constants: UPPER_SNAKE_CASE
- Private members: mPrefix (Java convention)

#### Error Handling
- Use try/catch blocks for exceptions
- Handle Android-specific exceptions (e.g., network, permissions)
- Use Android's error reporting mechanisms
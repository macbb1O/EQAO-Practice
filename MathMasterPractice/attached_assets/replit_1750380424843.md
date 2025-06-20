# EQAO Grade 9 Math Practice Test Generator

## Overview

This is a Streamlit-based web application that generates practice tests for the EQAO (Education Quality and Accountability Office) Grade 9 Mathematics Assessment. The application creates randomized multiple-choice tests with 54 questions distributed across Ontario's Grade 9 mathematics curriculum strands.

## System Architecture

The application follows a simple client-side architecture built with Streamlit:

- **Frontend**: Streamlit web interface for user interaction
- **Backend Logic**: Python modules handling question generation and curriculum mapping
- **Data Storage**: In-memory session state for test data (no persistent database)
- **Deployment**: Autoscale deployment on Replit infrastructure

## Key Components

### 1. Main Application (`app.py`)
- Streamlit web interface
- Session state management for test persistence
- User interaction controls (generate test, show/hide answers)
- Question display formatting

### 2. Question Generator (`question_generator.py`)
- Core logic for generating randomized math questions
- Implements proper strand distribution per EQAO requirements
- Creates both Group 1 and Group 2 question sets (27 questions each)
- Uses predefined data sets for realistic question contexts

### 3. Curriculum Mapping (`curriculum_strands.py`)
- Maps Ontario Grade 9 mathematics curriculum expectations
- Defines strand categories (Number Sense, Algebra, Data, Geometry, Financial Literacy)
- Provides structured curriculum expectations for question generation

### 4. Configuration Files
- `.replit`: Deployment and runtime configuration
- `pyproject.toml`: Python dependencies management
- `.streamlit/config.toml`: Streamlit server configuration

## Data Flow

1. **Test Generation**: User clicks generate button → QuestionGenerator creates 54 questions → Questions stored in session state
2. **Question Display**: Questions rendered with multiple choice options → Answers/explanations shown on demand
3. **Session Management**: All data maintained in Streamlit session state (no persistence between sessions)

## External Dependencies

### Core Dependencies
- **Streamlit (>=1.46.0)**: Web application framework
- **Python 3.11**: Runtime environment

### Additional Libraries (from uv.lock)
- **Altair**: Data visualization support
- **Blinker**: Signal handling
- **Cachetools**: Caching utilities
- Various supporting libraries for Streamlit functionality

## Deployment Strategy

- **Platform**: Replit with autoscale deployment target
- **Runtime**: Python 3.11 with Nix package management
- **Server**: Streamlit development server on port 5000
- **Configuration**: Headless server mode for production deployment

The application is designed for immediate deployment without additional setup or database configuration.

## Changelog

- June 20, 2025: Initial setup with 54-question generator
- June 20, 2025: Converted to interactive one-question-at-a-time format with immediate feedback
- June 20, 2025: Added index.html landing page for better user experience

## User Preferences

Preferred communication style: Simple, everyday language.
import streamlit as st
import random
from question_generator import QuestionGenerator
from curriculum_strands import STRAND_MAPPINGS

def initialize_session_state():
    """Initialize session state variables for the application."""
    if 'test_started' not in st.session_state:
        st.session_state.test_started = False
    if 'test_generated' not in st.session_state:
        st.session_state.test_generated = False
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'selected_answer' not in st.session_state:
        st.session_state.selected_answer = None
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answered_questions' not in st.session_state:
        st.session_state.answered_questions = []

def generate_new_test():
    """Generate a new practice test with 54 questions."""
    generator = QuestionGenerator()
    st.session_state.questions = generator.generate_full_test()
    st.session_state.test_generated = True
    st.session_state.test_started = True
    st.session_state.current_question = 0
    st.session_state.selected_answer = None
    st.session_state.show_result = False
    st.session_state.score = 0
    st.session_state.answered_questions = []

def display_interactive_question():
    """Display current question with interactive answer selection."""
    if not st.session_state.questions or st.session_state.current_question >= len(st.session_state.questions):
        return
    
    current_q = st.session_state.questions[st.session_state.current_question]
    question_num = st.session_state.current_question + 1
    
    # Progress indicator
    progress = st.session_state.current_question / len(st.session_state.questions)
    st.progress(progress)
    st.write(f"**Question {question_num} of {len(st.session_state.questions)}**")
    st.write(f"**Score: {st.session_state.score}/{len(st.session_state.answered_questions)}**")
    
    # Display question
    st.markdown(f"### Q{question_num}. ({current_q['strand']})")
    st.markdown(f"**{current_q['question']}**")
    
    # Extract just the option letters and text (remove the "A) ", "B) " etc.)
    options = []
    option_letters = []
    for option in current_q['options']:
        letter = option.split(')')[0]
        text = option.split(') ', 1)[1] if ') ' in option else option
        options.append(text)
        option_letters.append(letter)
    
    # Radio button for answer selection
    if not st.session_state.show_result:
        selected_index = st.radio(
            "Choose your answer:",
            range(len(options)),
            format_func=lambda x: f"{option_letters[x]}) {options[x]}",
            key=f"question_{question_num}",
            index=None
        )
        
        # Submit answer button
        if selected_index is not None:
            if st.button("Submit Answer", type="primary"):
                st.session_state.selected_answer = option_letters[selected_index]
                st.session_state.show_result = True
                st.rerun()
    else:
        # Show result
        correct_letter = current_q['answer'].split(')')[0]
        user_answer = st.session_state.selected_answer
        
        # Display user's answer
        for i, (letter, text) in enumerate(zip(option_letters, options)):
            if letter == user_answer:
                if letter == correct_letter:
                    st.success(f"✓ {letter}) {text} - Your answer (Correct!)")
                else:
                    st.error(f"✗ {letter}) {text} - Your answer (Incorrect)")
            elif letter == correct_letter:
                st.success(f"✓ {letter}) {text} - Correct answer")
            else:
                st.write(f"{letter}) {text}")
        
        # Show explanation
        st.info(f"**Explanation:** {current_q['explanation']}")
        
        # Update score if not already counted
        if st.session_state.current_question not in st.session_state.answered_questions:
            if user_answer == correct_letter:
                st.session_state.score += 1
            st.session_state.answered_questions.append(st.session_state.current_question)
        
        # Next question button
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.session_state.current_question < len(st.session_state.questions) - 1:
                if st.button("Next Question", type="primary"):
                    st.session_state.current_question += 1
                    st.session_state.selected_answer = None
                    st.session_state.show_result = False
                    st.rerun()
            else:
                if st.button("Finish Test", type="primary"):
                    show_final_results()
        
        with col2:
            if st.button("Review Previous"):
                if st.session_state.current_question > 0:
                    st.session_state.current_question -= 1
                    st.session_state.selected_answer = None
                    st.session_state.show_result = False
                    st.rerun()

def show_final_results():
    """Display final test results."""
    total_questions = len(st.session_state.questions)
    final_score = st.session_state.score
    percentage = round((final_score / total_questions) * 100, 1)
    
    st.balloons()
    st.success(f"Test Complete!")
    st.metric("Final Score", f"{final_score}/{total_questions}", f"{percentage}%")
    
    if percentage >= 80:
        st.success("Excellent work! You're well prepared for the EQAO test.")
    elif percentage >= 70:
        st.info("Good job! Keep practicing to improve your score.")
    elif percentage >= 60:
        st.warning("You're getting there! Review the topics you missed.")
    else:
        st.error("Keep studying! Focus on the areas where you need more practice.")

def show_welcome_screen():
    """Display welcome screen before starting the test."""
    st.title("📚 EQAO Grade 9 Math Practice Test")
    st.markdown("### Welcome to the interactive practice test!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Test Features:**
        - 54 unique multiple choice questions
        - Interactive one-question-at-a-time format
        - Immediate feedback and explanations
        - Progress tracking and scoring
        - Covers all curriculum strands
        - Fresh questions on every restart
        """)
    
    with col2:
        st.markdown("""
        **Curriculum Strands:**
        - Number Sense (5-6 questions per group)
        - Algebra (9-10 questions per group)
        - Data (4-5 questions per group)
        - Geometry & Measurement (4-5 questions per group)
        - Financial Literacy (3-4 questions per group)
        """)
    
    st.markdown("---")
    st.markdown("### Ready to begin?")
    st.markdown("The test contains 54 questions split into two groups of 27 questions each, just like the real EQAO assessment.")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Start Practice Test", type="primary", use_container_width=True):
            generate_new_test()
            st.rerun()

def main():
    st.set_page_config(
        page_title="EQAO Grade 9 Math Practice Test",
        page_icon="📚",
        layout="wide"
    )
    
    initialize_session_state()
    
    # Show welcome screen if test hasn't started
    if not st.session_state.test_started:
        show_welcome_screen()
        return
    
    # Main test interface
    st.title("📚 EQAO Grade 9 Math Practice Test")
    
    # Control buttons in sidebar
    with st.sidebar:
        st.markdown("### Test Controls")
        if st.button("🔄 Start New Test", type="primary"):
            st.session_state.test_started = False
            st.rerun()
        
        if st.session_state.test_generated and st.session_state.questions:
            st.markdown("---")
            st.markdown("### Progress")
            progress_percent = (st.session_state.current_question + 1) / len(st.session_state.questions)
            st.progress(progress_percent)
            st.write(f"Question {st.session_state.current_question + 1} of {len(st.session_state.questions)}")
            
            if len(st.session_state.answered_questions) > 0:
                st.write(f"Score: {st.session_state.score}/{len(st.session_state.answered_questions)}")
            
            st.markdown("---")
            st.markdown("### Test Structure")
            st.markdown("""
            - **Total Questions:** 54 multiple choice
            - **Strands:** Number Sense, Algebra, Data, Geometry, Financial Literacy
            - **Format:** Interactive one-at-a-time
            """)
    
    # Check if we're at the end of the test
    if (st.session_state.test_generated and 
        st.session_state.current_question >= len(st.session_state.questions)):
        show_final_results()
        
        # Option to restart
        if st.button("Take Another Test", type="primary"):
            st.session_state.test_started = False
            st.rerun()
    else:
        # Display current question
        if st.session_state.test_generated and st.session_state.questions:
            display_interactive_question()

if __name__ == "__main__":
    main()

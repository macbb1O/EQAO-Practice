"""
Ontario Grade 9 Mathematics Curriculum Expectations and Strand Mappings
Based on the EQAO Assessment Framework
"""

STRAND_MAPPINGS = {
    'B': 'Number Sense',
    'C': 'Algebra', 
    'D': 'Data',
    'E': 'Geometry and Measurement',
    'F': 'Financial Literacy'
}

# Curriculum expectations mapped to specific strands
CURRICULUM_EXPECTATIONS = {
    # Number Sense (Strand B)
    'B1.1': 'Development and Use of Numbers',
    'B1.2': 'Number Sets - subsets and relationships',
    'B1.3': 'Number Sets - density, infinity, and limit',
    'B2.1': 'Powers - patterns and scientific notation',
    'B2.2': 'Powers - operations and simplification',
    'B3.1': 'Rational Numbers - integers in context',
    'B3.2': 'Rational Numbers - unit fractions',
    'B3.3': 'Rational Numbers - positive and negative signs',
    'B3.4': 'Operations with fractions and mixed numbers',
    'B3.5': 'Rates, percentages, and proportions',
    
    # Algebra (Strand C)
    'C1.1': 'Development and Use of Algebra',
    'C1.2': 'Creating algebraic expressions',
    'C1.3': 'Comparing equivalent expressions',
    'C1.4': 'Simplifying algebraic expressions',
    'C1.5': 'Creating and solving equations',
    'C2.1': 'Coding - algebraic concepts',
    'C2.2': 'Coding - computational thinking',
    'C2.3': 'Coding - reading and modifying code',
    'C3.1': 'Linear and non-linear relations',
    'C3.2': 'Representing linear relations',
    'C3.3': 'Comparing linear relations',
    'C4.1': 'Characteristics of relations',
    'C4.2': 'Graphing equations and inequalities',
    'C4.3': 'Transformations of linear functions',
    'C4.4': 'Determining equations from graphs',
    
    # Data (Strand D)
    'D1.1': 'Data collection and implications',
    'D1.2': 'Statistical analysis of single variable',
    'D1.3': 'Scatter plots and correlation',
    'D2.1': 'Value of mathematical modelling',
    'D2.2': 'Identifying questions for data collection',
    'D2.3': 'Creating data collection plans',
    
    # Geometry and Measurement (Strand E) - Extended from typical Grade 9 expectations
    'E1.1': 'Geometric relationships and properties',
    'E1.2': 'Area and perimeter calculations',
    'E1.3': 'Volume and surface area',
    'E1.4': 'Pythagorean theorem applications',
    'E1.5': 'Similar triangles and scaling',
    'E2.1': 'Measurement conversions',
    'E2.2': 'Precision and accuracy',
    
    # Financial Literacy (Strand F) - Extended from typical Grade 9 expectations
    'F1.1': 'Simple and compound interest',
    'F1.2': 'Budgeting and financial planning',
    'F1.3': 'Consumer mathematics',
    'F1.4': 'Income and taxation',
    'F1.5': 'Saving and investing basics'
}

# Question distribution requirements per group of 27 questions
STRAND_DISTRIBUTION = {
    'B': (5, 6),  # Number Sense: 5-6 questions
    'C': (9, 10), # Algebra: 9-10 questions  
    'D': (4, 5),  # Data: 4-5 questions
    'E': (4, 5),  # Geometry: 4-5 questions
    'F': (3, 4)   # Financial: 3-4 questions
}

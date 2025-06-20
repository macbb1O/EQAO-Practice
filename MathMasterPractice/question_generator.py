import random
import math
from curriculum_strands import CURRICULUM_EXPECTATIONS, STRAND_DISTRIBUTION

class QuestionGenerator:
    def __init__(self):
        self.names = ["Alex", "Jordan", "Taylor", "Sam", "Casey", "Morgan", "Riley", "Avery", "Quinn", "Jamie",
                     "Maya", "Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Benjamin"]
        self.cities = ["Toronto", "Ottawa", "Hamilton", "London", "Windsor", "Kingston", "Sudbury", "Thunder Bay",
                      "Barrie", "Guelph", "Kitchener", "Waterloo", "Oshawa", "St. Catharines", "Cambridge"]
        self.items = ["books", "pencils", "notebooks", "markers", "folders", "calculators", "rulers", "erasers"]
        self.companies = ["TechCorp", "DataSoft", "InnovateCo", "FutureTech", "SmartSys", "NextGen", "ProTech"]
        
    def generate_full_test(self):
        """Generate a complete 54-question test with proper strand distribution."""
        questions = []
        
        # Generate Group 1 (27 questions)
        group1_questions = self.generate_group_questions()
        questions.extend(group1_questions)
        
        # Generate Group 2 (27 questions) 
        group2_questions = self.generate_group_questions()
        questions.extend(group2_questions)
        
        return questions
    
    def generate_group_questions(self):
        """Generate 27 questions for one group with proper strand distribution."""
        questions = []
        
        # Determine exact distribution for this group
        distribution = {}
        for strand, (min_q, max_q) in STRAND_DISTRIBUTION.items():
            distribution[strand] = random.randint(min_q, max_q)
        
        # Adjust if total doesn't equal 27
        total = sum(distribution.values())
        while total != 27:
            if total < 27:
                # Add questions to strands that haven't reached max
                candidates = [s for s, (min_q, max_q) in STRAND_DISTRIBUTION.items() 
                             if distribution[s] < max_q]
                if candidates:
                    strand = random.choice(candidates)
                    distribution[strand] += 1
                    total += 1
            else:
                # Remove questions from strands that are above minimum
                candidates = [s for s, (min_q, max_q) in STRAND_DISTRIBUTION.items() 
                             if distribution[s] > min_q]
                if candidates:
                    strand = random.choice(candidates)
                    distribution[strand] -= 1
                    total -= 1
        
        # Generate questions for each strand
        for strand, count in distribution.items():
            for _ in range(count):
                question = self.generate_question_by_strand(strand)
                questions.append(question)
        
        # Shuffle questions within the group
        random.shuffle(questions)
        return questions
    
    def generate_question_by_strand(self, strand):
        """Generate a question for a specific curriculum strand."""
        if strand == 'B':
            return random.choice([
                self.generate_powers_question,
                self.generate_rational_numbers_question,
                self.generate_scientific_notation_question,
                self.generate_fractions_question,
                self.generate_percentages_question
            ])()
        elif strand == 'C':
            return random.choice([
                self.generate_algebraic_expression_question,
                self.generate_equation_solving_question,
                self.generate_linear_relations_question,
                self.generate_graphing_question,
                self.generate_slope_question
            ])()
        elif strand == 'D':
            return random.choice([
                self.generate_statistics_question,
                self.generate_correlation_question,
                self.generate_data_analysis_question,
                self.generate_probability_question
            ])()
        elif strand == 'E':
            return random.choice([
                self.generate_geometry_question,
                self.generate_measurement_question,
                self.generate_pythagorean_question,
                self.generate_area_perimeter_question
            ])()
        elif strand == 'F':
            return random.choice([
                self.generate_interest_question,
                self.generate_budgeting_question,
                self.generate_consumer_math_question,
                self.generate_taxation_question
            ])()
    
    # Number Sense Questions (Strand B)
    def generate_powers_question(self):
        base = random.randint(2, 5)
        exp1 = random.randint(2, 4)
        exp2 = random.randint(2, 4)
        
        correct = base ** (exp1 + exp2)
        wrong1 = base ** (exp1 * exp2)
        wrong2 = (base ** exp1) + (base ** exp2)
        wrong3 = base ** (exp1 - exp2) if exp1 > exp2 else base ** (exp2 - exp1)
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'B2.2 – Operations with Powers',
            'question': f'What is the value of {base}^{exp1} × {base}^{exp2}?',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'Using the rule a^m × a^n = a^(m+n), we get {base}^{exp1+exp2} = {correct}.'
        }
    
    def generate_rational_numbers_question(self):
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)
        while num2 == 0:
            num2 = random.randint(-10, 10)
        
        correct = num1 + num2
        wrong1 = num1 - num2
        wrong2 = num1 * num2
        wrong3 = abs(num1) + abs(num2)
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'B3.1 – Integers in Context',
            'question': f'A temperature rises {num1}°C, then changes by {num2}°C. What is the total temperature change?',
            'options': [f'{chr(65+i)}) {options[i]}°C' for i in range(4)],
            'answer': f'{answer_letter}) {correct}°C',
            'explanation': f'Total change = {num1} + ({num2}) = {correct}°C.'
        }
    
    def generate_scientific_notation_question(self):
        coefficient = random.choice([1.2, 1.5, 2.3, 3.4, 4.7, 5.6, 6.8, 7.9, 8.1, 9.3])
        exponent = random.randint(3, 8)
        
        number = coefficient * (10 ** exponent)
        correct = f"{coefficient} × 10^{exponent}"
        wrong1 = f"{coefficient} × 10^{exponent-1}"
        wrong2 = f"{coefficient*10} × 10^{exponent-1}"
        wrong3 = f"{coefficient/10} × 10^{exponent+1}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'B2.1 – Scientific Notation',
            'question': f'Express {int(number):,} in scientific notation.',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'{int(number):,} = {correct} in scientific notation.'
        }
    
    def generate_fractions_question(self):
        num1, den1 = random.randint(1, 5), random.randint(2, 8)
        num2, den2 = random.randint(1, 5), random.randint(2, 8)
        
        # Find common denominator
        common_den = den1 * den2
        new_num1 = num1 * den2
        new_num2 = num2 * den1
        result_num = new_num1 + new_num2
        
        # Simplify if possible
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        common_factor = gcd(result_num, common_den)
        simplified_num = result_num // common_factor
        simplified_den = common_den // common_factor
        
        correct = f"{simplified_num}/{simplified_den}" if simplified_den != 1 else str(simplified_num)
        wrong1 = f"{result_num}/{common_den}"
        wrong2 = f"{num1 + num2}/{den1 + den2}"
        wrong3 = f"{new_num1 + new_num2}/{den1 + den2}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'B3.4 – Operations with Fractions',
            'question': f'What is {num1}/{den1} + {num2}/{den2}?',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'Convert to common denominator: {new_num1}/{common_den} + {new_num2}/{common_den} = {result_num}/{common_den} = {correct}.'
        }
    
    def generate_percentages_question(self):
        original = random.randint(200, 800)
        percent = random.choice([15, 20, 25, 30, 35, 40])
        
        correct = original * (percent / 100)
        wrong1 = original + percent
        wrong2 = original * percent
        wrong3 = original / percent
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        name = random.choice(self.names)
        
        return {
            'strand': f'B3.5 – Percentages and Proportions',
            'question': f'{name} saves {percent}% of their monthly income of ${original}. How much do they save?',
            'options': [f'{chr(65+i)}) ${options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) ${correct}',
            'explanation': f'{percent}% of ${original} = {percent/100} × ${original} = ${correct}.'
        }
    
    # Algebra Questions (Strand C)
    def generate_algebraic_expression_question(self):
        a = random.randint(2, 6)
        b = random.randint(1, 5)
        
        correct = f"{a}x + {b}"
        wrong1 = f"{a + b}x"
        wrong2 = f"{a}x - {b}"
        wrong3 = f"{b}x + {a}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'C1.2 – Creating Algebraic Expressions',
            'question': f'A number x is multiplied by {a}, then {b} is added. Which expression represents this?',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'Multiply by {a} gives {a}x, then add {b} gives {a}x + {b}.'
        }
    
    def generate_equation_solving_question(self):
        x_value = random.randint(2, 8)
        a = random.randint(2, 5)
        b = random.randint(1, 10)
        c = a * x_value + b
        
        correct = x_value
        wrong1 = x_value + 1
        wrong2 = x_value - 1
        wrong3 = c - b
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'C1.5 – Solving Equations',
            'question': f'Solve for x: {a}x + {b} = {c}',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'{a}x + {b} = {c} → {a}x = {c - b} → x = {correct}.'
        }
    
    def generate_linear_relations_question(self):
        m = random.randint(1, 5)
        b = random.randint(-5, 5)
        x = random.randint(1, 5)
        
        correct = m * x + b
        wrong1 = m * x - b
        wrong2 = m + x + b
        wrong3 = m * (x - b)
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'C3.2 – Linear Relations',
            'question': f'If y = {m}x + {b}, what is the value of y when x = {x}?',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'Substitute x = {x}: y = {m}({x}) + {b} = {m*x} + {b} = {correct}.'
        }
    
    def generate_graphing_question(self):
        m = random.randint(1, 4)
        b = random.randint(-3, 3)
        
        correct = f"slope = {m}, y-intercept = {b}"
        wrong1 = f"slope = {b}, y-intercept = {m}"
        wrong2 = f"slope = -{m}, y-intercept = {b}"
        wrong3 = f"slope = {m}, y-intercept = -{b}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'C4.4 – Linear Equations from Graphs',
            'question': f'What are the slope and y-intercept of the line y = {m}x + {b}?',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'In y = mx + b form, m = {m} (slope) and b = {b} (y-intercept).'
        }
    
    def generate_slope_question(self):
        x1, y1 = random.randint(1, 5), random.randint(1, 10)
        x2, y2 = random.randint(6, 10), random.randint(11, 20)
        
        correct = (y2 - y1) / (x2 - x1)
        wrong1 = (x2 - x1) / (y2 - y1)
        wrong2 = (y2 + y1) / (x2 + x1)
        wrong3 = (y2 - y1) / (x2 + x1)
        
        # Round to nearest integer or half for clean answers
        correct = round(correct * 2) / 2
        wrong1 = round(wrong1 * 2) / 2
        wrong2 = round(wrong2 * 2) / 2
        wrong3 = round(wrong3 * 2) / 2
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'C4.4 – Slope Calculation',
            'question': f'What is the slope of the line passing through points ({x1}, {y1}) and ({x2}, {y2})?',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'Slope = (y₂ - y₁)/(x₂ - x₁) = ({y2} - {y1})/({x2} - {x1}) = {correct}.'
        }
    
    # Data Questions (Strand D)
    def generate_statistics_question(self):
        data = sorted([random.randint(10, 90) for _ in range(7)])
        
        median = data[3]  # middle value of 7 numbers
        mean = sum(data) / len(data)
        mode = random.choice(data)  # simplified for this question
        range_val = max(data) - min(data)
        
        correct = median
        wrong1 = round(mean)
        wrong2 = mode
        wrong3 = range_val
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'D1.2 – Statistical Analysis',
            'question': f'Find the median of this data set: {", ".join(map(str, data))}',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'The median is the middle value when data is ordered: {median}.'
        }
    
    def generate_correlation_question(self):
        scenarios = [
            ("height and shoe size", "positive"),
            ("temperature and coat sales", "negative"), 
            ("study time and test scores", "positive"),
            ("car age and value", "negative")
        ]
        
        scenario, correct_corr = random.choice(scenarios)
        
        correct = f"{correct_corr} correlation"
        wrong1 = f"{'negative' if correct_corr == 'positive' else 'positive'} correlation"
        wrong2 = "no correlation"
        wrong3 = "perfect correlation"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'D1.3 – Correlation Analysis',
            'question': f'What type of correlation would you expect between {scenario}?',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'As one variable increases, the other {"increases" if correct_corr == "positive" else "decreases"}, showing {correct_corr} correlation.'
        }
    
    def generate_data_analysis_question(self):
        sample_size = random.randint(100, 500)
        percentage = random.randint(15, 85)
        
        correct = round(sample_size * percentage / 100)
        wrong1 = sample_size + percentage
        wrong2 = sample_size - percentage
        wrong3 = round(sample_size * percentage / 50)
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'D1.1 – Data Collection and Analysis',
            'question': f'In a survey of {sample_size} students, {percentage}% prefer online learning. How many students is this?',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'{percentage}% of {sample_size} = {percentage/100} × {sample_size} = {correct} students.'
        }
    
    def generate_probability_question(self):
        favorable = random.randint(2, 6)
        total = random.randint(favorable + 2, 12)
        
        correct = f"{favorable}/{total}"
        wrong1 = f"{total - favorable}/{total}"
        wrong2 = f"{favorable}/{total - favorable}"
        wrong3 = f"{total}/{favorable}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        color = random.choice(["red", "blue", "green", "yellow"])
        
        return {
            'strand': f'D1.3 – Probability',
            'question': f'A bag contains {total} balls, {favorable} of which are {color}. What is the probability of drawing a {color} ball?',
            'options': [f'{chr(65+i)}) {options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) {correct}',
            'explanation': f'Probability = favorable outcomes / total outcomes = {favorable}/{total}.'
        }
    
    # Geometry Questions (Strand E)
    def generate_geometry_question(self):
        angle1 = random.randint(30, 80)
        angle2 = random.randint(30, 80)
        
        correct = 180 - angle1 - angle2
        wrong1 = 180 - angle1
        wrong2 = angle1 + angle2
        wrong3 = 90 - angle1
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'E1.1 – Geometric Properties',
            'question': f'In a triangle, two angles measure {angle1}° and {angle2}°. What is the measure of the third angle?',
            'options': [f'{chr(65+i)}) {options[i]}°' for i in range(4)],
            'answer': f'{answer_letter}) {correct}°',
            'explanation': f'Sum of angles in a triangle = 180°. Third angle = 180° - {angle1}° - {angle2}° = {correct}°.'
        }
    
    def generate_measurement_question(self):
        length = random.randint(5, 15)
        width = random.randint(3, 10)
        
        correct = 2 * (length + width)
        wrong1 = length + width
        wrong2 = length * width
        wrong3 = 2 * length + width
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'E1.2 – Area and Perimeter',
            'question': f'What is the perimeter of a rectangle with length {length} cm and width {width} cm?',
            'options': [f'{chr(65+i)}) {options[i]} cm' for i in range(4)],
            'answer': f'{answer_letter}) {correct} cm',
            'explanation': f'Perimeter = 2(length + width) = 2({length} + {width}) = {correct} cm.'
        }
    
    def generate_pythagorean_question(self):
        a = random.randint(3, 8)
        b = random.randint(3, 8)
        c_squared = a*a + b*b
        c = round(math.sqrt(c_squared), 1)
        
        correct = c
        wrong1 = a + b
        wrong2 = round(math.sqrt(a*a - b*b), 1) if a > b else round(math.sqrt(b*b - a*a), 1)
        wrong3 = round(math.sqrt(c_squared + 1), 1)
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'E1.4 – Pythagorean Theorem',
            'question': f'In a right triangle, if the legs are {a} units and {b} units, what is the length of the hypotenuse?',
            'options': [f'{chr(65+i)}) {options[i]} units' for i in range(4)],
            'answer': f'{answer_letter}) {correct} units',
            'explanation': f'Using a² + b² = c²: {a}² + {b}² = {a*a} + {b*b} = {c_squared}, so c = {correct}.'
        }
    
    def generate_area_perimeter_question(self):
        radius = random.randint(3, 8)
        
        correct = round(math.pi * radius * radius, 1)
        wrong1 = round(2 * math.pi * radius, 1)
        wrong2 = round(math.pi * radius, 1)
        wrong3 = round(math.pi * radius * radius / 2, 1)
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        return {
            'strand': f'E1.2 – Area Calculations',
            'question': f'What is the area of a circle with radius {radius} units? (Use π ≈ 3.14)',
            'options': [f'{chr(65+i)}) {options[i]} square units' for i in range(4)],
            'answer': f'{answer_letter}) {correct} square units',
            'explanation': f'Area = πr² = π × {radius}² = π × {radius*radius} ≈ {correct} square units.'
        }
    
    # Financial Literacy Questions (Strand F)
    def generate_interest_question(self):
        principal = random.randint(500, 2000)
        rate = random.choice([2, 3, 4, 5, 6])
        time = random.randint(1, 5)
        
        correct = principal * (rate / 100) * time
        wrong1 = principal + (rate * time)
        wrong2 = principal * rate * time
        wrong3 = principal + correct
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        name = random.choice(self.names)
        
        return {
            'strand': f'F1.1 – Simple Interest',
            'question': f'{name} invests ${principal} at {rate}% simple interest for {time} years. How much interest is earned?',
            'options': [f'{chr(65+i)}) ${options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) ${correct}',
            'explanation': f'Simple Interest = P × r × t = ${principal} × {rate/100} × {time} = ${correct}.'
        }
    
    def generate_budgeting_question(self):
        income = random.randint(2000, 5000)
        housing_percent = random.randint(25, 35)
        
        correct = income * (housing_percent / 100)
        wrong1 = income - (housing_percent * 10)
        wrong2 = income / housing_percent
        wrong3 = income + (housing_percent * 10)
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        name = random.choice(self.names)
        
        return {
            'strand': f'F1.2 – Budgeting',
            'question': f'{name} earns ${income} monthly and spends {housing_percent}% on housing. How much is spent on housing?',
            'options': [f'{chr(65+i)}) ${options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) ${correct}',
            'explanation': f'{housing_percent}% of ${income} = {housing_percent/100} × ${income} = ${correct}.'
        }
    
    def generate_consumer_math_question(self):
        original_price = random.randint(50, 200)
        discount_percent = random.choice([10, 15, 20, 25, 30])
        
        discount_amount = original_price * (discount_percent / 100)
        correct = original_price - discount_amount
        wrong1 = original_price + discount_amount
        wrong2 = discount_amount
        wrong3 = original_price * (discount_percent / 100)
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        item = random.choice(self.items)
        
        return {
            'strand': f'F1.3 – Consumer Mathematics',
            'question': f'A set of {item} costs ${original_price}. With a {discount_percent}% discount, what is the sale price?',
            'options': [f'{chr(65+i)}) ${options[i]}' for i in range(4)],
            'answer': f'{answer_letter}) ${correct}',
            'explanation': f'Discount = ${original_price} × {discount_percent/100} = ${discount_amount}. Sale price = ${original_price} - ${discount_amount} = ${correct}.'
        }
    
    def generate_taxation_question(self):
        gross_income = random.randint(30000, 80000)
        tax_rate = random.choice([10, 12, 15, 18, 20])
        
        correct = gross_income * (tax_rate / 100)
        wrong1 = gross_income - (tax_rate * 100)
        wrong2 = gross_income + correct
        wrong3 = gross_income / tax_rate
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        answer_letter = chr(65 + options.index(correct))
        
        name = random.choice(self.names)
        
        return {
            'strand': f'F1.4 – Income and Taxation',
            'question': f'{name} has a gross income of ${gross_income:,} and pays {tax_rate}% in taxes. How much tax is paid?',
            'options': [f'{chr(65+i)}) ${options[i]:,}' for i in range(4)],
            'answer': f'{answer_letter}) ${correct:,}',
            'explanation': f'Tax = {tax_rate}% of ${gross_income:,} = {tax_rate/100} × ${gross_income:,} = ${correct:,}.'
        }


MAX_CONSTANTS = 10
propositions = ['p','q','r','s']
variables = ['x','y','z','w']
predicates = ['P','Q','R','S']

def is_propositional(fmla):
    if fmla == "":
        return 0
    # print(fmla)
    #negation
    if fmla[0] == '~':
        # print("negate")
        return is_propositional(fmla[1:])
    #binary connective
    elif fmla[0] == '(' and fmla[-1] == ')':
        # print("bracket")
        fmla = fmla[1:-1]
        left_bracket = 0
        right_bracket = 0
        for i in range(0,len(fmla)):
            if fmla[i] == '(':
                left_bracket += 1
            if fmla[i] == ')':
                right_bracket += 1
            if left_bracket == right_bracket:
                if fmla[i] == '/' or fmla[i] == '\\' or fmla[i] == '=':
                    # print("connective")
                    lhs = is_propositional(fmla[0:i])
                    # print("second")
                    rhs = is_propositional(fmla[i+2:])
                    if lhs + rhs == 2: return 1
                    else: return 0
    #propositons
    elif len(fmla) == 1 and fmla[0] in propositions:
        # print("prop")
        return 1
    return 0

def is_first_order(fmla):
    if fmla == "":
        return 0
    # print(fmla)
    #negation
    if fmla[0] == '~':
        # print("negate")
        return is_first_order(fmla[1:])
   #binary connective
    elif fmla[0] == '(' and fmla[-1] == ')':
        # print("bracket")
        fmla = fmla[1:-1]
        left_bracket = 0
        right_bracket = 0
        for i in range(0,len(fmla)):
            if fmla[i] == '(':
                left_bracket += 1
            if fmla[i] == ')':
                right_bracket += 1
            if left_bracket == right_bracket:
                if fmla[i] == '/' or fmla[i] == '\\' or fmla[i] == '=':
                    # print("connective")
                    lhs = is_first_order(fmla[0:i])
                    # print("second")
                    rhs = is_first_order(fmla[i+2:])
                    if lhs + rhs == 2: return 1
                    else: return 0
    #existentially quantified
    elif fmla[0] == 'E' and fmla[1] in variables:
        # print("ex")
        return is_first_order(fmla[2:])
    #universally quantified
    elif fmla[0] == 'A' and fmla[1] in variables:
        # print("ax")
        return is_first_order(fmla[2:])
    #predicates
    elif len(fmla) == 6 and fmla[0] in predicates and fmla[2] in variables and fmla[4] in variables:
        # print("prop")
        return 1
    return 0

# Parse a formula, consult parseOutputs for return values.
def parse(fmla):
    ##grammar - letter, ~, ( /\ ), P(x,y), Ey Az
    # print(is_propositional(fmla))
    # print(is_first_order(fmla))
    # 'not a formula'
    if is_first_order(fmla) + is_propositional(fmla) == 0:
        # print("here")
        return 0
    # 'an atom'
    if fmla[0] in predicates:
        return 1
    # 'a negation of a first order logic formula'
    if is_first_order(fmla) and fmla[0] == '~':
        return 2
    # 'a universally quantified formula'
    if fmla[0] == 'A':
        return 3
    # 'an existentially quantified formula'
    if fmla[0] == 'E':
        return 4
    # 'a binary connective first order formula'
    if is_first_order(fmla) and fmla[0] == '(':
        return 5
    # 'a proposition'
    if fmla[0] in propositions:
        return 6
    # 'a negation of a propositional formula'
    if is_propositional(fmla) and fmla[0] == '~':
        return 7
    # 'a binary connective propositional formula'
    if is_propositional(fmla) and fmla[0] == '(':
        return 8

# Return the LHS of a binary connective formula
def lhs(fmla):
    if fmla[0] == '(' and fmla[-1] == ')':
        # Remove outer parentheses
        fmla = fmla[1:-1]
    # Split the formula based on the binary connective
    left_bracket = 0
    right_bracket = 0
    for i in range(0,len(fmla)):
        # print(" letter %s, left %s, right %s." % (fmla[i], left_bracket ,right_bracket))
        if fmla[i] == '(':
            left_bracket += 1
        if fmla[i] == ')':
            right_bracket += 1
        if left_bracket == right_bracket:
            if fmla[i] == '/' or fmla[i] == '\\' or fmla[i] == '=':
                return fmla[0:i]

# Return the connective symbol of a binary connective formula
def con(fmla):
    if fmla[0] == '(' and fmla[-1] == ')':
        # Remove outer parentheses
        fmla = fmla[1:-1]
    # Split the formula based on the binary connective
    left_bracket = 0
    right_bracket = 0
    for i in range(0,len(fmla)):
        if fmla[i] == '(':
            left_bracket += 1
        if fmla[i] == ')':
            right_bracket += 1
        if left_bracket == right_bracket:
            if fmla[i] == '/' or fmla[i] == '\\' or fmla[i] == '=':
                return fmla[i:i+2]

# Return the RHS symbol of a binary connective formula
def rhs(fmla):
    if fmla[0] == '(' and fmla[-1] == ')':
        # Remove outer parentheses
        fmla = fmla[1:-1]
    # Split the formula based on the binary connective
    left_bracket = 0
    right_bracket = 0
    for i in range(0,len(fmla)):
        if fmla[i] == '(':
            left_bracket += 1
        if fmla[i] == ')':
            right_bracket += 1
        if left_bracket == right_bracket:
            if fmla[i] == '/' or fmla[i] == '\\' or fmla[i] == '=':
                return fmla[i+2:]


# You may choose to represent a theory as a set or a list
def theory(fmla):#initialise a theory with a single formula in it
    return [fmla]

def Exp(Σ):
     #check if each formula in Σ is an atom or its negation
    for i in Σ:
        if ((len(i) == 1 and i in propositions) or (len(i) == 2 and i[0] == '~') or (len(i) == 6 and i[0] in predicates) or (len(i) == 7 and i[0] == '~' and i[1] in predicates)) == 0:
            return 0
    return 1

def C(Σ):
    #check if each formula is atom or prop: if so then check if its negation exists
    for i in Σ:
        if (len(i) == 1 and i in propositions) or (len(i) == 6 and i[0] in predicates):
            i = '~' + i
            if i in Σ:
                return 1
    return 0

def is_alpha(current):
    parsed = parse(current)
    if parsed not in [2,5,7,8]:
        return 0
    if parsed in [5,8] and con(current) == '/\\':
        return 1
    if parsed in [2,7]:
        current = current[1:]
        parsed = parse(current)
        if parsed in [2,7]:
            return 1
        if parsed in [5,8] and con(current) == '\\/':
            return 1
        if parsed in [5,8] and con(current) == '=>':
            return 1
    return 0

def is_beta(current):
    parsed = parse(current)
    if parsed not in [2,5,7,8]:
        return 0
    if parsed in [5,8] and con(current) == '\\/':
        return 1
    if parsed in [5,8] and con(current) == '=>':
        return 1
    if parsed in [2,7]:
        current = current[1:]
        parsed = parse(current)
        if parsed in [5,8] and con(current) == '/\\':
            return 1
    return 0

def is_delta(current):
    parsed = parse(current)
    if parsed not in [2,4,7]:
        return 0
    if parsed == 4:
        return 1
    if parsed in [2,7]:
        current = current[1:]
        parsed = parse(current)
        if parsed == 3:
            return 1
    return 0
     
def is_gamma(current):
    parsed = parse(current)
    if parsed not in [2,3,7]:
        return 0
    if parsed == 3:
        return 1
    if parsed in [2,7]:
        current = current[1:]
        parsed = parse(current)
        if parsed == 4:
            return 1
    return 0
    
def alpha_exp(Σ,current):
    # print("a")
    parsed = parse(current)
    if parsed in [5,8] and con(current) == '/\\':
        Σ.append(lhs(current))
        Σ.append(rhs(current))
    if parsed in [2,7]:
        current = current[1:]
        parsed = parse(current)
        if parsed in [2,7]:
            Σ.append(current[1:])
        if parsed in [5,8] and con(current) == '\\/':
            Σ.append('~' + lhs(current))
            Σ.append('~' + rhs(current))    
        if parsed in [5,8] and con(current) == '=>':
            Σ.append(lhs(current))
            Σ.append('~' + rhs(current)) 
    return Σ
     
def beta_exp(Σ,current):
    # print("b")
    parsed = parse(current)
    Σ_beta = [Σ.copy(),Σ]
    if parsed in [5,8] and con(current) == '\\/':
        Σ_beta[0].append(lhs(current))
        Σ_beta[1].append(rhs(current))
    if parsed in [5,8] and con(current) == '=>':
        Σ_beta[0].append('~' + lhs(current))
        Σ_beta[1].append(rhs(current))
    if parsed in [2,7]:
        current = current[1:]
        parsed = parse(current)
        if parsed in [5,8] and con(current) == '/\\':
            Σ_beta[0].append('~' + lhs(current))
            Σ_beta[1].append('~' + rhs(current))    
    return Σ_beta

def delta_exp(Σ,current,constants):
    # print("d")
    new = ["a","b","c","d","e","f","g",'h','i','j','k']
    global variables
    variables.append(new[constants])
    parsed = parse(current)
    if parsed == 4:
        old = current[1]
        current = current.replace(old,new[constants])
        Σ.append(current[2:])
    if parsed in [2,7]:
        current = current[1:]
        parsed = parse(current)
        if parsed == 3:
            old = current[1]
            current = current.replace(old,new[constants])
            Σ.append('~' + current[2:])
    return Σ

def gamma_exp(Σ,current,cons):
    # print("y")
    new = ["a","b","c","d","e","f","g",'h','i','j','k']
    Σ.append(current)
    parsed = parse(current)
    if parsed == 3:
        old = current[1]
        current = current.replace(old,new[cons])
        Σ.append(current[2:])
    if parsed in [2,7]:
        current = current[1:]
        parsed = parse(current)
        if parsed == 4:
            old = current[1]
            current = current.replace(old,new[cons])
            Σ.append('~' + current[2:])
    return Σ

def gamma_add(current,cons):
    # print("y2")
    new = ["a","b","c","d","e","f","g",'h','i','j','k']
    parsed = parse(current)
    if parsed == 3:
        old = current[1]
        current = current.replace(old,new[cons])
        return current[2:]
    if parsed in [2,7]:
        current = current[1:]
        parsed = parse(current)
        if parsed == 4:
            old = current[1]
            current = current.replace(old,new[cons])
            return '~' + current[2:]
# def gamma_cons():
#     #figure out what gamma constant to use
#     # if constants = -1 then find variable in formula and use that
#     return 0

#check for satisfiability
def sat(tableau):
    gamma_count = 0
    constants = -1
    while len(tableau):
        # print(tableau)
        Σ = tableau[0]
        tableau = tableau[1:]
        if Exp(Σ) and (not C(Σ)):
            return 1
        else:
            first_a = ""
            first_b = ""
            first_d = ""
            first_y = ""
            for i in range(0,len(Σ)):
                if ((len(Σ[i]) == 1 and Σ[i] in propositions) or (len(Σ[i]) == 2 and Σ[i][0] == '~') or (len(Σ[i]) == 6 and Σ[i][0] in predicates) or (len(Σ[i]) == 7 and Σ[i][0] == '~' and Σ[i][1] in predicates)) == 0:
                    if is_alpha(Σ[i]):
                        first_a = i
                        break
            for i in range(0,len(Σ)):
                if ((len(Σ[i]) == 1 and Σ[i] in propositions) or (len(Σ[i]) == 2 and Σ[i][0] == '~') or (len(Σ[i]) == 6 and Σ[i][0] in predicates) or (len(Σ[i]) == 7 and Σ[i][0] == '~' and Σ[i][1] in predicates)) == 0:
                    if is_beta(Σ[i]):
                        first_b = i
                        break
            for i in range(0,len(Σ)):
                if ((len(Σ[i]) == 1 and Σ[i] in propositions) or (len(Σ[i]) == 2 and Σ[i][0] == '~') or (len(Σ[i]) == 6 and Σ[i][0] in predicates) or (len(Σ[i]) == 7 and Σ[i][0] == '~' and Σ[i][1] in predicates)) == 0:
                    if is_delta(Σ[i]):
                        first_d = i
                        break
            for i in range(0,len(Σ)):
                if ((len(Σ[i]) == 1 and Σ[i] in propositions) or (len(Σ[i]) == 2 and Σ[i][0] == '~') or (len(Σ[i]) == 6 and Σ[i][0] in predicates) or (len(Σ[i]) == 7 and Σ[i][0] == '~' and Σ[i][1] in predicates)) == 0:
                    if is_gamma(Σ[i]):
                        first_y = i
                        break
            if first_a != "":
                    current = Σ.pop(first_a)
            elif first_d != "":
                    current = Σ.pop(first_d)
            elif first_b != "":
                    current = Σ.pop(first_b)
            else:
                    current = Σ.pop(first_y)            

            if is_alpha(current):
                Σ = alpha_exp(Σ,current)
            if is_beta(current):
                Σ_b = beta_exp(Σ,current)
                Σ = Σ_b[0]
                if Σ not in tableau and not C(Σ):
                    tableau.append(Σ)
                Σ = Σ_b[1]
            if is_delta(current):
                constants += 1
                Σ = delta_exp(Σ,current,constants)
            if is_gamma(current):
                gamma_count += 1
                # gamma_index = 0
                # cons = gamma_cons(constants)
                #gamma index -1 and check first using gammma acons
                # Σ = gamma_exp(Σ,current,0)
                for i in range(0,constants + 1):
                    if gamma_add(current,i) not in Σ:
                        Σ = gamma_exp(Σ,current,i)
                        # print(Σ)
                        break

            if Σ not in tableau and not C(Σ):
                # print("%s not in %s" % (Σ, tableau))
                tableau.append(Σ)
            if gamma_count > 100:
                #need to properly check if in endless loop...ran out of new constants to use
                return 1
            if constants >= 10:
                return 2
    
    if len(tableau) == 0:
            return 0

#output 0 if not satisfiable, output 1 if satisfiable, output 2 if number of constants exceeds MAX_CONSTANTS

#DO NOT MODIFY THE CODE BELOW
f = open('input.txt')

parseOutputs = ['not a formula',
                'an atom',
                'a negation of a first order logic formula',
                'a universally quantified formula',
                'an existentially quantified formula',
                'a binary connective first order formula',
                'a proposition',
                'a negation of a propositional formula',
                'a binary connective propositional formula']

satOutput = ['is not satisfiable', 'is satisfiable', 'may or may not be satisfiable']



firstline = f.readline()

PARSE = False
if 'PARSE' in firstline:
    PARSE = True

SAT = False
if 'SAT' in firstline:
    SAT = True

for line in f:
    variables = ['x','y','z','w']
    if line[-1] == '\n':
        line = line[:-1]
    parsed = parse(line)

    if PARSE:
        output = "%s is %s." % (line, parseOutputs[parsed])
        if parsed in [5,8]:
            output += " Its left hand side is %s, its connective is %s, and its right hand side is %s." % (lhs(line), con(line) ,rhs(line))
        print(output)

    if SAT:
        if parsed:
            tableau = [theory(line)]
            print('%s %s.' % (line, satOutput[sat(tableau)]))
        else:
            print('%s is not a formula.' % line)

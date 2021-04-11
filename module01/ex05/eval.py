class Evaluator:
    @staticmethod
    def zip_evaluate(words,coefs):
        if(len(words)!=len(coefs)):
            return -1
        else:
            result=0
            x=list(zip(words,coefs))
            for i in range(len(x)):
                result+=len(x[i][0])*x[i][1]
            return result
                
    @staticmethod
    def enumerate_evaluate(words,coefs):
        if(len(words)!=len(coefs)):
            return -1
        else:
            result=0
            x=list(enumerate(words))
            for i in range(len(x)):
                result+=len(x[i][1])*coefs[i]
            return result
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

val = Evaluator.zip_evaluate(words, coefs)
print(val)
val = Evaluator.enumerate_evaluate(words, coefs)
print(val)
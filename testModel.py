from model import model

mdl=model.Model()
dstnc= 3500

mdl.buildGraph(dstnc)
print(mdl.getNumNodi(),mdl.getNumArchi())
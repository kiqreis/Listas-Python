import numpy as np
from sklearn.ensemble import RandomForestClassifier

def classifica(treino , classes, teste):
    clf = RandomForestClassifier(random_state = 0)
    X = treino
    y = classes
    clf.fit(X, y)
    assert(clf.predict(X) == np.array(y)).all()
    return list(clf.predict(teste))


if __name__ == '__main__':
    classifica()

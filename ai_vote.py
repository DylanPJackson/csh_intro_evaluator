"""
    filename : ai_vote.py
    description : Use the CSH Introductory Evaluator for yourself to see what
        house would vote, based off of past data.
    author : Dylan P. Jackson
"""
import numpy as  np
import sys
from scipy.special import expit 

def sigmoid(z):
    """
        Perform sigmoid function on z

        Parameters
        ----------
        z : numpy array (n,)
            Array of n students, each with weights already applied to their features 

        Returns
        -------
        numpy array (n,)
            Array with sigmoid applied to each element
    """
    # Using expit to suppress RuntimeWarning of overflow
    return (1.0 / (1.0 + expit(-z)))

def predict(theta, X, powers):
    """
        Place each x of X into a tertiary classification based off of given
        powers and theta

        Parameters (I describe shape with (rows, cols), contrary to numpy)
        ----------
        theta : numpy array (3,6) 
            The weights which are applied to each row of X in order to place
            each row into a tertiary classification
        X : numpy array (n,6)
            The features of each student. Each student is represented by six
            features, but this function allows for n number of students to be
            classified in one function call
        powers : numpy array (1,6)
            The exponents to raise each feature in each x of X as part of the
            hypothesis function

        Returns
        -------
        numpy array (n)
            The array of predictions for each student. These are either 0,1,2.
            0 means fail, 1 means pass, 2 means conditional. 
    """
    hypotheses = sigmoid(np.power(X,powers).dot(theta.T))
    predictions = np.argmax(hypotheses, axis=1)

    return predictions

def display_results(preds, names):
    """
        Pretty print the predicted votes
        
        Parameters
        ----------
        preds : array (n)
            Array of predictions for each of the names
        names : array (n)
            The names of all the people put through the classifier
    """
    m = preds.shape[0]
    for i in range(m):
        pred = preds[i]
        name = names[i]
        if pred == 0:
            print(name + " would fail. Congratulations or I'm sorry!")
        elif pred == 1:
            print(name + " would pass. Congratulations or I'm sorry!")
        elif pred == 2:
            print(name + " would get a conditional. Congratulations or I'm sorry!")

def main():
    X = ""
    names = ""
    theta = np.array([[-.94707612, .0935797, .21562864, -.06362213, -.0705111, -1.06748832],
                      [.37619398, -.10531447, -.06600369, .07863234, .0143614, 1.69845091],
                      [-2.51165427, .11899932, -1.59840977, -.13111087, .21506235, -2.90024353]])
    powers = np.array([0,2,4,4,0,0])
    num_args = len(sys.argv)
    # Minor help if given incorrect amount of args
    if (num_args < 3) or (num_args > 7):
        print("python ai_vote.py -f filename\n" \
              "python ai_vote.py s_m h_m d_a t_a s\n" \
              "    s_m : signatures missed\n    h_m : house meetings missed\n" \
              "    d_a : directorship meetings attended\n    t_a : technical seminars attended\n" \
              "    s : social events (1 if attended any, 0 if none)")
    # If loading from a file
    elif (num_args == 3) and (sys.argv[1] == '-f'):
        data_path = sys.argv[2]
        X = np.loadtxt(data_path, delimiter = ",", usecols=(1,2,3,4,5))
        names = np.loadtxt(data_path, delimiter = ",", usecols = 0, dtype='str') 
        m = X.shape[0]
        if len(X.shape) == 1:
            X = X.reshape(1,m)
            m = X.shape[0]
        X = np.concatenate([np.ones((m,1)), X], axis=1)
    # If using command line exclusively (only supports one person this way tho)
    elif num_args == 7:
        X = np.array((1,float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])))
        X = X.reshape(1,6)
        names = [sys.argv[1]]
    # Get the predictions
    preds = predict(theta, X, powers)
    # Display them through command line
    display_results(preds, names) 

main()

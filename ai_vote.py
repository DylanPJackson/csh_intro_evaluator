"""
    filename : ai_vote.py
    description : Use the CSH Introductory Evaluator for yourself to see what
        house would vote, based off of past data.
    author : Dylan P. Jackson

    TODO : Define usage statement
           Take in command line features
           Load in features from file
           Pretty print response to user
"""
import numpy as  np
import sys
sys.path.insert(1,"../ai_implementations")
import custom_ai_utils

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
    hypotheses = custom_ai_utils.sigmoid(np.power(X,powers).dot(all_theta.T))
    predictions = np.argmax(predictions, axis=1)

    return predictions

def main():
    theta = np.array([[-.94707612, .0935797, .21562864, -.06362213, -.0705111, -1.06748832],
                      [.37619398, -.10531447, -.06600369, .07863234, .0143614, 1.69845091],
                      [-2.51165427, .11899932, -1.59840977, -.13111087, .21506235, -2.90024353]])
    powers = np.array([0,2,4,4,0,0])
    num_args = len(sys.argv)
    if (num_args < 3) or (num_args > 7):
        print("python ai_vote.py -f filename\n" \
              "python ai_vote.py s_m h_m d_a t_a s\n" \
              "    s_m : signatures missed\n    h_m : house meetings missed\n" \
              "    d_a : directorship meetings attended\n    t_a : technical seminars attended\n" \
              "    s : social events (1 if attended any, 0 if none)")

main()

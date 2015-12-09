#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []


    for i in range(0, len(predictions)):
        error = abs(net_worths[i] - predictions[i])

        tup_data = (ages[i], net_worths[i], error)
        cleaned_data.append(tup_data)

    print('Length of cleaned_data after error calculation: {0}'.format(len(cleaned_data)))
    cleaned_data = sorted(cleaned_data, key=lambda tup: tup[2])
    print('Length of cleaned_data after sort by error: {0}'.format(len(cleaned_data)))

    # Return only 90%
    new_len = int(len(cleaned_data) * 0.9)
    print('New length after stripping 10%: {0}'.format(new_len))
    cleaned_data = cleaned_data[:new_len]
    print('Length of cleaned_data after stripping 10%: {0}'.format(len(cleaned_data)))
    ### your code goes here

    
    return cleaned_data


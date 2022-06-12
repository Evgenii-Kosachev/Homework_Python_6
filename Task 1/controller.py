import inOutData
import calculation

def Script():
    line1 = inOutData.ReadData('Task 1/Data/first_polynomial.txt')
    line2 = inOutData.ReadData('Task 1/Data/second_polynomial.txt')

    calculation.InterpolationString(line1, line2)
    result = None

    inOutData.WriteData(None)  # Str

# Не доделал
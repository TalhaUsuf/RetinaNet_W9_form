import base64
from pydantic import BaseModel


class verify_inp(BaseModel):
    picture: str


def encode(data : verify_inp):
    """
    takes in a string path

    Parameters
    ----------
    picture

    Returns
    -------

    """
    print(data)
    picture=data.dict()["picture"]
    with open(picture, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())  # base64 encoding
        my_string = my_string.decode('utf-8')  # decoding to 'utf-8' standard format
        my_string1 = str(my_string)  # converting to string

        # f1.write(my_string1)

        return my_string1


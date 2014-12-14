#!/usr/bin/env python


def request_user_input(prompt, validator=None):
    try:
        response = None
        while(response is None):
            response = raw_input(prompt)
            if validator:
                while not validator(response):
                    response = raw_input(prompt)
        return response

    except (EOFError, KeyboardInterrupt):
        return None


def first_prompt_validator(response):
    return response == u"1" or response == u"2"


def full_name_validator(response):
    if response == 'list':
        print donor_dict.keys()
    return type(response) == str and " " in response


def donation_validator(response):
    try:
        response = int(response)
    except ValueError:
        print "Donation amount must be an integer"
    finally:
        return type(response) == int and response > 0

if __name__ == '__main__':
    donor_dict = {'Richard Sherman': [25, 50, 100], 'Russell Wilson': [30, 50],
                  'Marshawn Lynch': [60, 75], 'Kam Chancellor': [20],
                  'Doug Baldwin': [10]}

    first_response = request_user_input(u'To Send a Thank You, enter 1 '
                                        'To Create a Report, enter 2: ',
                                        first_prompt_validator)

    if first_response == u"1":
        thank_you_name = request_user_input(
            'Enter the full name of the donor to thank: ', full_name_validator)

        donation_amount = request_user_input(
            'Enter the donation amount (must be an integer value): ',
            donation_validator)
        donation_amount = int(donation_amount)

        donor_dict.setdefault(thank_you_name, []).append(donation_amount)

        print """\nDear %s,\n
        Thank you for your generous donation of %i dollars.
        Your support allows our charity to continue to serve the community.\n
        Thank You,\n\tPete Carroll\n\tCharity Director""" % (
            thank_you_name, donation_amount)
        # elif first_response == "report":"""

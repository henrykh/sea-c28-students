#!/usr/bin/env python


def request_user_input(prompt, validator=None):
    try:
        response = raw_input(prompt)
        if response == u'return':
            return response
        if validator:
            while not validator(response):
                response = raw_input(prompt)
                if response == 'return':
                    break
        return response

    except (EOFError, KeyboardInterrupt):
        return None


def first_prompt_validator(response):
    return response == u"1" or response == u"2" or response == u"3"


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

    first_response = ""
    while first_response != u"3":
        first_response = request_user_input(u'\nTo Send a Thank You, enter 1.\n'
                                            'To Create a Report, enter 2.\n'
                                            'To quit, enter 3: \n',
                                            first_prompt_validator)

        if first_response == u"1":
            thank_you_name = request_user_input(
                '\nEnter the full name of the donor to thank\n'
                '(or enter "return" to quit current task): \n',
                full_name_validator)
            if thank_you_name == 'return':
                continue

            donation_amount = request_user_input(
                '\nEnter the donation amount (must be an integer value greater than 0)\n'
                '(or enter "return" to quit current task): \n',
                donation_validator)
            if donation_amount == 'return':
                continue
            donation_amount = int(donation_amount)

            donor_dict.setdefault(thank_you_name, []).append(donation_amount)

            thank_you_msg = "\nDear %s,\n" % thank_you_name
            thank_you_msg += "\nThank you for your generous donation of %d dollars.\n" % donation_amount
            thank_you_msg += "Your support allows our charity to continue to serve the community.\n"
            thank_you_msg += "\nThank You,\nPete Carroll\nCharity Director\n"

            print thank_you_msg

        elif first_response == u"2":
            donor_data = {donor:
                          [sum(donor_dict[donor]),
                           len(donor_dict[donor]),
                           sum(donor_dict[donor]) /
                           float(len(donor_dict[donor]))]
                          for donor in donor_dict}
            donor_data_sorted = sorted(donor_data.items(),
                                       key=lambda (k, v): v[0], reverse=True)
            print "\n{:<20s} {:<20s} {:<25s} {:<20s}\n".format(
                'Donor Name', 'Total Donation',
                'Number of Donations', 'Average Donation')
            for donor in donor_data_sorted:
                donor = donor[0]
                print "{:<20s} {:>14d} {:>25d} {:>22.2f}\n".format(
                    donor, donor_data[donor][0],
                    donor_data[donor][1], donor_data[donor][2])

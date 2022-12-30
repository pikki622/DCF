def prettyprint(dcfs, years):
    '''
    Pretty print-out results of a DCF query.
    Handles formatting for all output variatisons.
    '''
    if years > 1:
        for k, v in dcfs.items():
            print(f'ticker: {k}')
            if len(dcfs[k].keys()) > 1:
                for yr, dcf in v.items():
                    print('date: {} \
                        \nvalue: {}'.format(yr, dcf))
    else:
        for k, v in dcfs.items():
            print('ticker: {}  \
                  \nvalue: {}'.format(k, v))

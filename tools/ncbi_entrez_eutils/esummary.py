#!/usr/bin/env python
import argparse
import eutils


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ESummary', epilog='')
    parser.add_argument('db', help='Database to use')
    parser.add_argument('--id_list', help='list of ids')
    parser.add_argument('--id', help='Comma separated individual IDs')
    parser.add_argument('--history_file', help='Filter existing history')
    args = parser.parse_args()

    c = eutils.Client(history_file=args.history_file)

    merged_ids = c.parse_ids(args.id_list, args.id, args.history_file)

    payload = {
        'db': args.db,
    }

    if args.history_file is not None:
        payload.update(c.get_history())
    else:
        payload['id'] = ','.join(merged_ids)

    print c.summary(**payload)
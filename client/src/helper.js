import minimist from 'minimist';

const defaultArguments = {
  id: {
    keys: ['id', 'i', 'switch-id', 'location-id'],
    defaultValue: null,
  },
  items_per_page: {
    keys: ['items-per-page', 'items'],
    defaultValue: 20,
  },
  page: {
    keys: ['p', 'page'],
    defaultValue: 1,
  },
};

const argumentParser = (args, validArguments) => {
  let parsedArguments = minimist(args);
  let query = {};
  if (!validArguments.every((key) => Object.keys(defaultArguments))) {
    throw Error(
      'defaultArguments does not contain all items inside of validArguments'
    );
  }

  validArguments.forEach((key) => {
    let defArg = defaultArguments[key];
    let value = null;
    defArg.keys.forEach((defKey) => {
      value = parsedArguments[defKey] ?? value;
    });
    query[key] = value ?? defArg.defaultValue;
  });

  return query;
};

/** Dont expect some high-level validator here, its just checking if exists or not, not validating the type */
export const argValidator = (args, validArguments) => {
  let query = argumentParser(args, validArguments);
  let valid = Object.keys(query).every((key) => query[key] != null);

  return {
    valid,
    ...query,
  };
};

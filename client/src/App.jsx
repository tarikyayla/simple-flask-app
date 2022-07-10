import './App.css';
import Terminal from 'react-console-emulator';
import { argValidator } from './helper';
import { get_locations, get_switches, get_location, get_ports } from './api';
import React, { useState } from 'react';
import { Loading } from './loading';

const Table = ({ rawData }) => {
  console.log('data -->', rawData);
  if (rawData == null || rawData.length === 0) {
    return 'Returns empty';
  }

  const head = Object.keys(rawData[0]);
  return (
    <table>
      <tr>
        {head.map((key) => (
          <th>{key}</th>
        ))}
      </tr>
      {rawData.map((row, index) => (
        <tr key={index}>
          {head.map((key) => {
            let isObject = row[key].constructor === Object;
            let value = isObject ? row[key].id : row[key];
            return <td>{value}</td>;
          })}
        </tr>
      ))}
    </table>
  );
};

const MyTerminal = () => {
  const [isLoading, setIsLoading] = useState(false);

  const commandCall = async (args, reqArgs, apiCall) => {
    const validArguments = argValidator(args, reqArgs);

    if (!validArguments.valid)
      return 'Command is not valid. Please use help for details';

    setIsLoading(true);
    let returnValue;
    try {
      const response = await apiCall(validArguments);
      returnValue = <Table rawData={response.data} />;
    } catch {
      returnValue = 'An error happened. Please check logs';
    }
    setIsLoading(false);
    return returnValue;
  };
  
  const commands = {
    locations: {
      description: 'Get the list of locations -> ',
      usage: 'locations --items-per-page <int> --page <int>',
      fn: (...args) =>
        commandCall(args, ['items_per_page', 'page'], get_locations),
    },
    location: {
      description: 'Get location entity -> ',
      usage: 'location --id <int>',
      fn: (...args) => commandCall(args, ['id'], get_location),
    },
    switches: {
      description: 'Get the list of switches -> ',
      usage: 'switches --location-id <int> --items-per-page <int> --page <int>',
      fn: (...args) =>
        commandCall(args, ['id', 'items_per_page', 'page'], get_switches),
    },
    ports: {
      description: 'Get the list of ports -> ',
      usage: 'ports --switch-id <int> --items-per-page <int> --page <int>',
      fn: (...args) =>
        commandCall(args, ['id', 'items_per_page', 'page'], get_ports),
    },
  };

  return (
    <React.Fragment>
      {isLoading && <Loading />}
      <Terminal
        className="terminal-container"
        contentClassName="content"
        commands={commands}
        promptLabel={'tarik@localhost:$'}
      />
    </React.Fragment>
  );
};

function App() {
  return (
    <div className="App">
      <MyTerminal />
    </div>
  );
}

export default App;

import { GymList } from '../GymList';

import './App.css';

const dummyGyms = [
  {
    title: 'Supergym New York',
    id: 123,
    address: {
      city: 'New York City',
      zip: '12345',
      street: 'Main St 12',
    },
  },
  {
    title: 'BrooklynBros',
    id: 345,
    address: {
      city: 'New York City',
      zip: '34567',
      street: 'Bro-klyn 99',
    },
  },
  {
    title: 'PumpNation Berlin',
    id: 234,
    address: {
      city: 'Berlin',
      zip: '23456',
      street: 'Merkelallee 1',
    },
  },
  // mock loading gym:
  undefined,
];

export function App() {
  return (
    <div className="App theme-light">
      <div className="stack stack-xl">
        <header className="App-header">
          <div className="container">
            <h1 className="title title-xl">Find your gym</h1>
          </div>
        </header>

        <main>
          <div className="container">
            <GymList gyms={dummyGyms} />
          </div>
        </main>
      </div>
    </div>
  );
}

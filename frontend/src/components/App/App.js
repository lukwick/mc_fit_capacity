import { GymItem } from '../GymItem/GymItem';

import './App.css';

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
            <GymItem
              title="Supergym New York"
              id={123}
              address={{
                city: 'New York City',
                zip: '12345',
                street: 'Main St 12',
              }}></GymItem>
          </div>
        </main>
      </div>
    </div>
  );
}

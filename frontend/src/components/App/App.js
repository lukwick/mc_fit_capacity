import { GymList } from '../GymList';
import { useState } from 'react';

import './App.css';

export function App() {
  const [gyms, setGyms] = useState([undefined, undefined]);

  useState(() => {
    fetchGyms().then((gyms) => {
      setGyms(gyms);
    });
  }, []);

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
            <GymList gyms={gyms} />
          </div>
        </main>
      </div>
    </div>
  );
}

async function fetchGyms() {
  // TODO: replace with env variable
  const DOMAIN = 'http://localhost:5000';
  const url = `${DOMAIN}/studios`;
  const request = await fetch(url);
  console.log(request);
  const gyms = await request.json();
  return gyms.map((gym) => ({
    ...gym,
    title: gym.name,
  }));
}

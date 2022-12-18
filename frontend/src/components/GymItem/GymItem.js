import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

import './GymItem.css';

export function GymItem({ id, title, address }) {
  const [isLoading, setIsLoading] = useState(false);
  const [capacity, setCapacity] = useState(undefined);
  const [level, setLevel] = useState(undefined);

  useEffect(() => {
    if (capacity === undefined) return;

    let level;
    if (capacity <= 30) level = 'low';
    else if (capacity >= 70) level = 'high';
    else level = 'medium';

    setLevel(level);
  }, [capacity]);

  const handleClick = () => {
    setIsLoading(true);
    fetchCapacity(id).then((capacity) => {
      setCapacity(capacity);
    });
  };

  const isSkeleton = !id || !title || !address;

  const headerContents = !isSkeleton ? (
    <>
      <h2 className="title title-m">{title}</h2>
      <address>{`${address.street}, ${address.zip} ${address.city}`}</address>
    </>
  ) : (
    <>
      <div>
        <div className="skeleton title title-m">
          Skeleton title while loading
        </div>
      </div>
      <div>
        <div className="skeleton">Skeleton address</div>
      </div>
    </>
  );

  return (
    <article className="GymItem theme-dark">
      <header className="stack stack-s">{headerContents}</header>

      <div>
        {!capacity && (
          <button
            className={`button button-full ${isSkeleton ? 'skeleton' : ''}`}
            onClick={handleClick}
            disabled={isLoading || isSkeleton}>
            {!isLoading ? 'Check capacity' : 'Loading...'}
          </button>
        )}

        {capacity && (
          <p className="GymItem-capacity">
            Current capacity:{' '}
            <span className={`GymItem-level GymItem-level-${level}`}>
              {capacity}%
            </span>
          </p>
        )}
      </div>
    </article>
  );
}

GymItem.propTypes = {
  title: PropTypes.string,
  id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  address: PropTypes.shape({
    city: PropTypes.string.isRequired,
    zip: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
    street: PropTypes.string.isRequired,
  }),
};

async function fetchCapacity(gymId) {
  // TODO: replace with env variable
  const DOMAIN = 'http://localhost:5000';
  const url = `${DOMAIN}/studios/${gymId}/capacity`;
  const request = await fetch(url);
  const { current } = await request.json();
  return current;
}

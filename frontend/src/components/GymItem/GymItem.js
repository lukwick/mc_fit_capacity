import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

import './GymItem.css';

export function GymItem({ id, title, address }) {
  const { city, street, zip } = address;
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
    // TODO: fetch
    setCapacity(20);
  };

  return (
    <article className="GymItem theme-dark">
      <header className="stack stack-s">
        <h2 className="title title-m">{title}</h2>
        <address>{`${street}, ${zip} ${city}`}</address>
      </header>

      <div>
        {!capacity && (
          <button
            className="button button-full"
            onClick={handleClick}
            disabled={isLoading}>
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
  title: PropTypes.string.isRequired,
  id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
  address: PropTypes.shape({
    city: PropTypes.string.isRequired,
    zip: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
    street: PropTypes.string.isRequired,
  }).isRequired,
};

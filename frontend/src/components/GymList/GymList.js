import { GymItem } from '../GymItem';
import PropTypes from 'prop-types';

export function GymList({ gyms }) {
  return (
    <div className="GymList">
      <ul className="stack stack-s">
        {gyms.map((gym) => (
          <li>
            <GymItem {...gym} />
          </li>
        ))}
      </ul>
    </div>
  );
}

GymList.propTypes = {
  gyms: PropTypes.arrayOf(GymItem.propTypes),
};

GymList.defaultProps = {
  gyms: [],
};

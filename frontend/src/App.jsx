import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [checkedItems, setCheckedItems] = useState({
    item1: false,
    item2: false,
    item3: false,
  });

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen);
  };

  const handleCheckboxChange = (item) => {
    setCheckedItems({
      ...checkedItems,
      [item]: !checkedItems[item],
    });
  };

  return (
    <div className="sidebar">
      <div className="dropdown">
        <button onClick={toggleDropdown} className="dropdown-button">
          {dropdownOpen ? 'Hide Options' : 'Show Options'}
        </button>
        {dropdownOpen && (
          <div className="dropdown-list">
            {Object.keys(checkedItems).map((item) => (
              <label key={item} className="dropdown-item">
                <input
                  type="checkbox"
                  checked={checkedItems[item]}
                  onChange={() => handleCheckboxChange(item)}
                />
                {item}
              </label>
            ))}
          </div>
        )}
      </div>

      <div className="search-bar">
        <input
          type="text"
          placeholder="Search..."
          value={searchTerm}
          onChange={handleSearchChange}
        />
      </div>
    </div>
  );
};

export default App

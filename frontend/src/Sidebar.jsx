import { useState } from 'react';

const Sidebar = ({ cryptos, selectedCryptos, onSelectionChange }) => {
    const [searchTerm, setSearchTerm] = useState('');

    // Filter cryptos based on the search term
    const filteredCryptos = cryptos.filter(crypto =>
        crypto.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
    };

    const handleCheckboxChange = (cryptoId) => {
        onSelectionChange(cryptoId);
    };

    return (
        <div className="sidebar">
            <input
                type="text"
                placeholder="Search Cryptos"
                value={searchTerm}
                onChange={handleSearchChange}
            />
            <div className="crypto-list">
                {filteredCryptos.map(crypto => (
                    <div key={crypto.id} className="crypto-item">
                        <input
                            type="checkbox"
                            id={crypto.id}
                            checked={selectedCryptos.includes(crypto.id)}
                            onChange={() => handleCheckboxChange(crypto.id)}
                        />
                        <label htmlFor={crypto.id}>{crypto.name}</label>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Sidebar;

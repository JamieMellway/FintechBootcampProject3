pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract payForProperty{
    uint public accountBalance;
    
    function sendPayment(address payable to, address from, uint256 amount) public {
        require(from == msg.sender, "Only the buyer sends coins");
        to.transfer(amount);
        accountBalance = address(this).balance;
    }

    function deposit() public payable {
        accountBalance = address(this).balance;
    }

    function () external payable {}
}

contract PropertyRegistry is ERC721Full, payForProperty {
    constructor() public ERC721Full("PropertyRegistryToken", "HOME") {}

    address payable contractAddress = address(uint160(address(this)));

    struct Property {
        address owner;
        string geoAddress;
        string propType;
        uint256 appraisalValue;
        string propJson;
    }

    // propCollection will act as a 'dictionary' of all Property (value), and their tokenId (key)
    mapping(uint256 => Property) public propCollection;

    event Appraisal(uint256 tokenId, uint256 appraisalValue, string reportURI, string propJson);
    
    function imageUri(
        uint256 tokenId
    ) public view returns (string memory propJson){
        return propCollection[tokenId].propJson;
    }

    function registerProperty(
        address payable owner,
        string memory geoAddress,
        string memory propType,
        uint256 initialAppraisalValue,
        string memory tokenURI,
        string memory tokenJSON
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        setApprovalForAll(contractAddress, true);

        _setTokenURI(tokenId, tokenURI);

        propCollection[tokenId] = Property(owner, geoAddress, propType, initialAppraisalValue, tokenJSON);

        return tokenId;
    }

    function buyProperty(uint256 token_id) public {
        address buyer_address = msg.sender;
        address payable seller_address = address(uint160(ownerOf(token_id)));
        uint256 amount = propCollection[token_id].appraisalValue;

        require(buyer_address != seller_address, "Sellers cannot buy their own property");

        sendPayment(seller_address, buyer_address, amount);
        safeTransferFrom(seller_address, buyer_address, token_id);
    }

    function newAppraisal(
        uint256 tokenId,
        uint256 newAppraisalValue,
        string memory reportURI,
        string memory tokenJSON
        
    ) public returns (uint256) {
        propCollection[tokenId].appraisalValue = newAppraisalValue;

        emit Appraisal(tokenId, newAppraisalValue, reportURI, tokenJSON);

        return (propCollection[tokenId].appraisalValue);
    }
}

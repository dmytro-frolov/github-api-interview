import React, { Component } from 'react';
import {
    Button,
    ButtonGroup,
    Row,
    Col,
    Container,
    Card,
    Form,
    InputGroup,
    FormControl,
    Navbar,
    Nav } from 'react-bootstrap';
  
import API from '../api'
import Serializer from '../serializer'
import {profileInfo} from '../templates'


class UserSearch extends Component {
    state = {
      username: "",
      isLoading: false,
    }
  
    changeUsernameHandler = (e) => {
      this.setState({username: e.target.value});
    }
  
    fetchUsernameInfo = () => {
      let username = this.state.username;

      let api = new API(this.props.accessToken);
      let req = api.fetchUsernameInfo(username);
      req.then((userInfoDict)=>{
        this.props.onGetUserInfo(userInfoDict);
        this.setState({username: userInfoDict.login})
      });
    }

    componentDidMount(){
      this.fetchUsernameInfo();
    }

    render() {
      return (
      <div>
        <label htmlFor="userSearch">Username</label>
        <InputGroup className="mb-3" id="userSearch" onChange={this.changeUsernameHandler}>
          <FormControl
            placeholder="Username"
            defaultValue={this.state.username}
          />
          <InputGroup.Append>
            <Button variant="outline-secondary" onClick={this.fetchUsernameInfo}>Search</Button>
          </InputGroup.Append>
        </InputGroup>
      </div>
      )
    };
  }


class UserAvatar extends Component {
  render(){
   return <img className="userAvatar" src={this.props.url}/> 
  }
}


class UserInfoPanel extends Component {
    state = {
        userInfoList: []
    }

    details = () => {
      let info = this.props.userInfoDict;
      let inputBoxes = {
        Name: info.name,
        Company: info.company,
        Blog: info.blog,
        Location: info.location,
        email: info.email,
        twitter: info.twitter_username,
        Bio: info.bio
      };

      let textBoxesList = [];
      Object.entries(inputBoxes).forEach(([key,value]) => {
        textBoxesList.push(this._inputTextbox(key, value));
      });

      return textBoxesList;
    }

    _inputTextbox = (key, value) => {
      return (
        <div>
          <label>{key}</label>
          <InputGroup>
              <Form.Control defaultValue={value} value={value}/>
          </InputGroup>
        </div>
      )
    }

    renderUserInfoFromJson() {
        let serializer = new Serializer()
        let template = profileInfo;
        return serializer.transform(this.props.userInfoDict, template)
    }

    render() {
        return (
            <div className="InfoPanel">{this.details()}</div>
        )
    }
  }


export {UserInfoPanel, UserSearch, UserAvatar}
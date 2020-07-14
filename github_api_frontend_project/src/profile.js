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
  
import API from './api'
import Serializer from './serializer'
import {profileInfo} from './templates'


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
      });
    }

    render() {
      return (
      <div>
        <label htmlFor="userSearch">Username</label>
        <InputGroup className="mb-3" id="userSearch" onChange={this.changeUsernameHandler}>
          <FormControl
            placeholder="Username"
          />
          <InputGroup.Append>
            <Button variant="outline-secondary" onClick={this.fetchUsernameInfo}>Search</Button>
          </InputGroup.Append>
        </InputGroup>
      </div>
      )
    };
  }


class UserInfoPanel extends Component {
    state = {
        userInfoList: []
    }

    renderUserInfoFromJson() {
        let serializer = new Serializer()
        let template = {
            "name": "input"
        }
        return serializer.transform(this.props.userInfoDict, template)
    }

    render() {
        return (
            <div>{this.renderUserInfoFromJson()}</div>
        )
    }
  }


export {UserInfoPanel, UserSearch}
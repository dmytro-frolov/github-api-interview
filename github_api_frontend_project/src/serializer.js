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


class Serializer {
    _fromDict = (inputDict) => {
        /*
        Json example from the backend:
        {
            "name": "Tom",
            "avatar": "http://example.com/avatar.jpg",
            "profile_url": "http://example.com/tom",
            "visible": true,
        }
        */
        this.data = inputDict
    }

    _readTemplate = (inputDict) => {
        /*
        Template example:
        {
            "name": "input",
            "avatar": "pic",
            "profile_url": "link",
            "visible": "checkbox",
            "login": "ro_input",
            "type": "null"
        }
        */
       //todo: type validation
       this.template = inputDict;
    }

    _get_type = (input_type, key, value) => {
        let type_map = {
            "input": 
                (<div><label htmlFor="userSearch">{key}</label>
                <InputGroup>
                    <Form.Control key={key} defaultValue={value} value={value}/>
                </InputGroup></div>),
            "ro_input": (<div><label htmlFor="userSearch">{key}</label>
                <InputGroup>
                    <Form.Control key={key} readOnly plaintext  defaultValue={value} />
                </InputGroup></div>),
            "link": <a href={value}>{key}</a>,
            "pic": <Form.Control key={key} defaultValue={value} />,
            "label": <div>{key}: {value}</div>,
            "null": <input type="hidden" key={key} name={key} value={value}/> 


        }
        
        return type_map[input_type]
    }

    transform = (inputData, template) => {
        this._fromDict(inputData);
        this._readTemplate(template);

        let result = [];
        Object.entries(inputData).forEach(([key,value]) => {
            let templateType = this.template[key];
            result.push(this._get_type(templateType, key, value));
        })

        return result
    }
}


export default Serializer;

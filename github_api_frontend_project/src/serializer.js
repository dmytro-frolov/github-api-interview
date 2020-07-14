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
            "visible": "checkbox"
        }
        */
       //todo: type validation
       this.template = inputDict;
    }

    _get_type = (input_type, value, comp_key) => {
        let type_map = {
            "input": <Form.Control key={comp_key} defaultValue={value} />,

        }
        
        return type_map[input_type]
    }

    transform = (inputData, template) => {
        this._fromDict(inputData);
        this._readTemplate(template);

        let result = [];
        Object.entries(inputData).forEach(([key,value]) => {
            let templateType = this.template[key];
            result.push(this._get_type(templateType, value, key));
        })

        return result
    }
}


export default Serializer;

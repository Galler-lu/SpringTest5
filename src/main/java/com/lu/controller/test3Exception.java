package com.lu.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class test3Exception {
    @RequestMapping("/testException")
    public String testException(){
        System.out.println(1/0);
        return "success";
    }
}

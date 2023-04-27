package com.lu.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class test2Interceptor {
    @RequestMapping("/hello")
    public String hello(){
        return "hello";
    }
    @RequestMapping("/testInterceptor")
    public String testInterceptor(){
        return "success";
    }
}

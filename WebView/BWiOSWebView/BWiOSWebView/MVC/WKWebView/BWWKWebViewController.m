//
//  BWWKWebViewController.m
//  BWiOSWebView
//
//  Created by BobWong on 2017/3/14.
//  Copyright © 2017年 BobWong. All rights reserved.
//

#import "BWWKWebViewController.h"
#import <WebKit/WebKit.h>

@interface BWWKWebViewController ()

@property (strong, nonatomic) WKWebView *webView;  ///< WebView

@end

@implementation BWWKWebViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [self.view addSubview:self.webView];
}

- (WKWebView *)webView {
    if (!_webView) {
        <#statements#>
    }
    return _webView;
}

@end

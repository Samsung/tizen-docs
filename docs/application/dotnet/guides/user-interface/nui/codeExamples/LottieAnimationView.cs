using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace NUIXamlSimpleApp
{
	public partial class XamlPage : ContentPage
	{
        public XamlPage()
        {
            InitializeComponent();
            lottie.URL = Tizen.Applications.Application.Current.DirectoryInfo.Resource + "lottieTest.json";
            lottie.Play();
        }
	}
}

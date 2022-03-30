using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;
using System.Linq;

namespace NUIXamlSimpleApp
{
    public partial class XamlPage : ContentPage
    {
        public XamlPage()
        {
            InitializeComponent();
            var resources_path = Tizen.Applications.Application.Current.DirectoryInfo.Resource;
            loading.ImageArray = Enumerable.Range(0, 12).Select(x => $"{resources_path}images/progress_{x}.png").ToArray();
            loading.Stop();
        }
        private void onBtnClicked(object sender, ClickedEventArgs e)
        {
            loading.Play();
        }
    }
}

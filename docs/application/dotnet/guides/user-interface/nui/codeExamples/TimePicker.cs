using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace NUIXamlSimpleApp
{
    public partial class XamlPage : ContentPage
    {
        private DateTime time;
        public XamlPage()
        {
            InitializeComponent();
            time = DateTime.Now;
            picker.Time=time;
        }
    }
}

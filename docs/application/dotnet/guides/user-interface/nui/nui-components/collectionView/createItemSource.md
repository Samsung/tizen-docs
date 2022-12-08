## Create item source

To use `CollectionView`, item source need to be created firstly:

1. Create an model class of item data:
    ```csharp
    class Animal
    {
        private string _name;
        private string _scientificName;
        private string _imageResource;
        private string _imageUrl = Tizen.Applications.Application.Current.DirectoryInfo.Resource + "animals/";

        public Animal(string name, string scientificName, string imageResource)
        {
            _name = name;
            _scientificName = scientificName;
            _imageResource = imageResource;
        }

        public string Name
        {
            get => _name;
            set => _name = value;
        }

        public string ScientificName
        {
            get => _scientificName;
            set => _scientificName = value;
        }

        public string ImagePath
        {
            get => _imageUrl + _imageResource;
        }
    }
    ```
    To apply properties changes dynamically in the CollectionView, you need to implement `INotifyPropertyChanged` interface.

    ```csharp
    class Animal : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler PropertyChanged;

        public string Name
        {
            get => _name;
            set
            {
                _name = value;
                //Invoke property changed event when property changed.
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("Name"));
            }
        }
    }
    ```

2. Create `IEnumerable` data collection for items:

    ```csharp
    var animals = new List<Animal>();
    animals.Add(new Animal("Cat", "Felis catus", "cat.png"));
    animals.Add(new Animal("Dog", "Canis lupus familiaris", "dog.png"));
    animals.Add(new Animal("Fox", "Vulpes" "fox.png"));
    animals.Add(new Animal("Horse", "Equus ferus", "horse.png"));
    ```

    To apply data changes dynamically in the CollectionView, you need to implement `INotifyPropertyChanged` and `INotifyCollectionChanged` interface.

    ```csharp
    var animals = new ObservableCollection<Animal>();
    ```

## Create grouped item source

CollectionView support grouped item source with `ObservableCollection<T>`:
1. Create `ObservableCollection<T>` data collection for group:

    ```csharp
    class Family : ObservableCollection<Animal>
    {
        private string _name;
        public Family(string name)
        {
            _name = name;
        }

        public Name
        {
            get => _name;
            set
            {
                _name = value;
                OnPropertyChanged(new PropertyChangedEventArgs("Name"));
            }
        }
    }
   ```
2. add group into group collection:

    ```csharp

    var families = new ObservableCollection<Family>();

    var falidae = new Family("Falidae");
    falidae.Add(new Animal("Cat", "Felis catus", "cat.png"));
    falidae.Add(new Animal("Cheetah", "Acinonyx jubatus", "cheetah.png"));
    falidae.Add(new Animal("Leopard", "Panthera pardus", "leopard.png"));
    falidae.Add(new Animal("Lion", "Panthera leo", "lion.png"));
    falidae.Add(new Animal("Tiger", "Panthera tigris", "tiger.png"));
    families.Add(falidae);

    var canidae = new Family("Canidae");
    canidae.Add(new Animal("Coyote", "Canis latrans" "coyote.png"));
    canidae.Add(new Animal("Dog", "Canis lupus familiaris", "dog.png"));
    canidae.Add(new Animal("Fox", "Vulpes" "fox.png"));
    canidae.Add(new Animal("Raccoon dog", "Nyctereutes procyonoides" "raccoondog.png"));
    canidae.Add(new Animal("Wolf", "Canis lupus" "wolf.png"));
    families.Add(canidae);
    ```
